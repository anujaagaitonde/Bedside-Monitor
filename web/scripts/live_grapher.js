const urlParams = new URLSearchParams(window.location.search);
let userUID = urlParams.get("UserID");

var livebutton = document.getElementById('livebutton');
livebutton.href = "./live_patient.html?UserID=" + userUID
var historybutton = document.getElementById('historybutton');
historybutton.href = "./patient_history.html?UserID=" + userUID



firebase
  .database()
  .ref("/")
  .on("value", function (snapshot) {
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

var RefArray = [];
function initChart(labels, values, id, title, primarycolor, yaxislabel) {
  var chartConfig = {
    labels: [],
    datasets: [
      {
        label: title,
        fill: false,
        lineTension: 0.1,
        backgroundColor: primarycolor,
        borderColor: primarycolor,
        borderCapStyle: "butt",
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: "miter",
        pointBorderColor: "rgba(75,192,192,1)",
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(75,192,192,1)",
        pointHoverBorderColor: "rgba(220,220,220,1)",
        pointHoverBorderWidth: 2,
        pointRadius: 0,
        pointHitRadius: 10,
        data: [],
        spanGaps: false,
        borderWidth: 6
      }
    ]
  };
  chartConfig.labels = labels;
  chartConfig.datasets[0].data = values;
  var ctx = document.getElementById(id).getContext("2d");
  var options = {
    maintainAspectRatio: false,
    tooltips: {
      enabled: false
    },
    title: {
      display: false,
      text: title
    },
    legend: {
      display: false
    },
    scales: {
      xAxes: [
        {
          ticks: {
            display: false
          },
          gridLines: {
            color: "#FFFFFF",
            lineWidth: 0.1
            // display: false
          }
        }
      ],
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: yaxislabel
          },
          gridLines: {
            // display: false
            color: "#FFFFFF",
            lineWidth: 0.1
          }
        }
      ]
    }
  };
  Chart.defaults.global.defaultFontColor = "white";
  RefArray[id] = new Chart(ctx, {
    type: "line",
    data: chartConfig,
    options: options
  });
}

function updateChart(label, value, id) {
  RefArray[id].data.labels.push(label);
  RefArray[id].data.datasets.forEach(dataset => {
    dataset.data.push(value);
  });
  RefArray[id].update();
}

function getChartData() {
  var templabels = [];
  var tempvalues = [];
  var ecglabels = [];
  var ecgvalues = [];
  var ppglabels = [];
  var ppgvalues = [];
  initChart(templabels, tempvalues, "tempChart", "Temperature Chart", "#3cd82c", "°C");
  initChart(ecglabels, ecgvalues, "ecgChart", "ECG Chart", "#59eaed", "mV");
  initChart(ppglabels, ppgvalues, "ppgChart", "PPG Chart", "#f51a18", "ppg vals");
  var temperatureref = firebase
    .database()
    .ref(userUID + "/temperatureSensor");
  temperatureref.on("child_added", function (ret, prevChildKey) {
    updateChart(prevChildKey, ret.val(), "tempChart");
  });
  var ecgref = firebase
    .database()
    .ref(userUID + "/ecgSensor");
  ecgref.on("child_added", function (ret, prevChildKey) {
    updateChart(prevChildKey, ret.val(), "ecgChart");
  });
  var ppgref = firebase
    .database()
    .ref(userUID + "/ppgSensor");
  ppgref.on("child_added", function (ret, prevChildKey) {
    updateChart(prevChildKey, ret.val(), "ppgChart");
  });
}
window.onload = getChartData();
