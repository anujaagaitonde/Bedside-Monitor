// Initialize Firebase
const urlParams = new URLSearchParams(window.location.search);
let userUID = urlParams.get("UserID");
window.onload = function(){
  var livebutton = document.getElementById('livebutton');
  livebutton.href = "./live_patient.html?UserID=" + userUID
  var historybutton = document.getElementById('historybutton');
  historybutton.href = "./patient_history.html?UserID=" + userUID 
}

var g=""
var g1=""
var g2=""

Date.prototype.toShortFormat = function () {
  var month_names = ["Jan", "Feb", "Mar",
    "Apr", "May", "Jun",
    "Jul", "Aug", "Sep",
    "Oct", "Nov", "Dec"];

  var day = this.getDate();
  var month_index = this.getMonth();
  var year = this.getFullYear();
  var hours = this.getHours();
  var minutes = this.getMinutes();
  var seconds = this.getSeconds();

  return "" + day + "-" + month_names[month_index] + "-" + year + " " + hours +":"+minutes+":"+seconds;
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
    <img src=${patientinfo.imageURL} class="profile_pic">

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

function zoomAndHighlight(inputdate){
  formattedDate = (new Date(parseInt(inputdate))).getTime()
  // window.alert(formattedDate-36000)
  desired_range = [formattedDate - 30000, formattedDate + 30000];
  animate();
}
function approach_range() {
  if (!desired_range) return;
  // go halfway there
  var range = g2.xAxisRange();
  if (Math.abs(desired_range[0] - range[0]) < 60 &&
    Math.abs(desired_range[1] - range[1]) < 60) {
    g.updateOptions({ dateWindow: desired_range });
    g1.updateOptions({ dateWindow: desired_range });
    g2.updateOptions({ dateWindow: desired_range });
    // (do not set another timeout.)
  } else {
    var new_range;
    new_range = [0.5 * (desired_range[0] + range[0]),
    0.5 * (desired_range[1] + range[1])];
    g.updateOptions({ dateWindow: new_range });
    g1.updateOptions({ dateWindow: new_range });
    g2.updateOptions({ dateWindow: new_range });
    animate();
  }
}

var reset = function () {
  var event = new MouseEvent('dblclick', {
    'view': window,
    'bubbles': true,
    'cancelable': true
  });
  document.getElementById('tempChart').dispatchEvent(event);
  document.getElementById('spO2Chart').dispatchEvent(event);
  document.getElementById('ppgChart').dispatchEvent(event);
};

animate = function () {
  setTimeout(approach_range, 5);
};



function buttonHTMLGenerator(inputdate){
  formattedDate = (new Date(parseInt(inputdate))).toShortFormat()
  return `
  <Button id=\"$(inputdate)\" onclick=zoomAndHighlight(${inputdate})>${formattedDate}</Button>`
}
async function main(){
  var tempdata = await getData("temperatureSensor");
  var ecgdata = await getData("ecgSensor");
  var ppgdata = await getData("ppgSensor");
   g = new Dygraph(document.getElementById("tempChart"), tempdata,
    {
      drawPoints: true,
      showRoller: false,
      strokeWidth: 1,
      color:"#3cd82c",
      labels: ['Time', 'Temperature'],
      connectSeparatedPoints: false
    });
  g1 = new Dygraph(document.getElementById("spO2Chart"), ecgdata,
    {
      drawPoints: true,
      showRoller: false,
      animatedZooms: true,
      strokeWidth: 1,
      color: "#59eaed",
      labels: ['Time', 'ecg']
    });
  g2 = new Dygraph(document.getElementById("ppgChart"), ppgdata,
    {
      drawPoints: true,
      showRoller: false,
      animatedZooms: true,
      strokeWidth: 1,
      color: "#f51a18",
      labels: ['Time', 'ppg']
    });

  firebase
    .database()
    .ref("/critical/"+userUID)
    .once("value", function (snapshot) {
      timestamps  = Object.keys(snapshot.val())
      for (var index in timestamps){
              document.getElementById("criticalTimes").innerHTML += buttonHTMLGenerator(timestamps[index])
      }
      document.getElementById("criticalTimes").innerHTML += `<button onclick=reset()> Reset </button>`

    });

}
main().then(() => {document.getElementsByClassName("loader")[0].style.display = "none";
document.getElementsByClassName("chartContainer")[0].style.display = "flex"});



// window.onload = getChartData();
