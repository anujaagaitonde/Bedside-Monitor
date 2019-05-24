// Initialize Firebase
const urlParams = new URLSearchParams(window.location.search);
let userUID = urlParams.get("UserID");
window.onload = function(){
  var livebutton = document.getElementById('livebutton');
  livebutton.href = "./live_patient.html?UserID=" + userUID
  var historybutton = document.getElementById('historybutton');
  historybutton.href = "./patient_history.html?UserID=" + userUID 
}



firebase
  .database()
  .ref("/")
  .once("value", function (snapshot) {
    let patientInfo = snapshot.val()[userUID]["patientInfo"];
    document.getElementById("patient_info").innerHTML += PatientHTMLGenerator(
      patientInfo
    );
  });
function PatientHTMLGenerator(patientinfo) {
  return `
    <img src="images/profile_pic.png" class="profile_pic">

    <div class="patient_id">
        <ul>
            <li><b>Name: </b>${patientinfo.Name}</li>
            <li><b>DOB: </b>${patientinfo.DOB}</li>
        </ul>
    </div>
    <div class="patient_status">
        <ul>
            <li><b>Abnormality detected: </b>${patientinfo.Abnormality}</li>
            <li><b>Condition: </b>${patientinfo.Condition} </li>
        </ul>
    </div>
    `;
}

function dateFormatter(unix_timestamp){
  var date = new Date(parseInt(unix_timestamp) );
  return date;
}

function getData(sensor) {
  var ref = firebase
    .database()
    .ref(userUID + "/"+sensor);
  return new Promise(function(resolve,reject){
    ref.once("value", function (ret) {
      input = ret.val()
    }).then(() => {
      var data = Object.keys(input).map(function (key) {
        return [dateFormatter(Number(key)), parseInt(input[key])];
      });
      resolve(data)
    })
  })
}

async function main(){
  var tempdata = await getData("temperatureSensor");
  var spo2data = await getData("spo2Sensor");
  var ppgdata = await getData("ppgSensor");
  var g = new Dygraph(document.getElementById("tempChart"), tempdata,
    {
      drawPoints: true,
      showRoller: false,
      labels: ['Time', 'Temperature']
    });
  var g1 = new Dygraph(document.getElementById("spO2Chart"), spo2data,
    {
      drawPoints: true,
      showRoller: false,
      labels: ['Time', 'Spo2']
    });
  var g2 = new Dygraph(document.getElementById("ppgChart"), ppgdata,
    {
      drawPoints: true,
      showRoller: false,
      labels: ['Time', 'ppg']
    });
}
main();



// window.onload = getChartData();
