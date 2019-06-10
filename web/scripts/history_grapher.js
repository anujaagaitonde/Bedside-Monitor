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

function filtergaps(raw) {
  for (var i in raw) {
    try {
      var diff = raw[parseInt(i)][0] - raw[parseInt(i) + 1][0]
      if (Math.abs(diff) > 50000) {
        raw[parseInt(i)][1] = Number.NaN
      }
    } catch {
      console.log("index error")
    }
  }
  return raw;
}

function getData(sensor) {
  var ref = firebase
    .database()
    .ref(userUID + "/"+sensor);
  return new Promise(function(resolve,reject){
    ref.once("value", function (ret) {
      input = ret.val()
    }).then(() => {
      try {
        var data = Object.keys(input).map(function (key) {
          return [dateFormatter(Number(key)), parseInt(input[key])];
        });
        resolve(filtergaps(data))
      } catch {
        resolve([])
      }
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
      strokeWidth: 1,
      color:"#3cd82c",
      labels: ['Time', 'Temperature'],
      connectSeparatedPoints: false
    });
  var g1 = new Dygraph(document.getElementById("spO2Chart"), spo2data,
    {
      drawPoints: true,
      showRoller: false,
      strokeWidth: 1,
      color: "#59eaed",
      labels: ['Time', 'Spo2']
    });
  var g2 = new Dygraph(document.getElementById("ppgChart"), ppgdata,
    {
      drawPoints: true,
      showRoller: false,
      strokeWidth: 1,
      color: "#f51a18",
      labels: ['Time', 'ppg']
    });
}
main().then(() => {document.getElementsByClassName("loader")[0].style.display = "none";
document.getElementsByClassName("chartContainer")[0].style.display = "flex"});



// window.onload = getChartData();
