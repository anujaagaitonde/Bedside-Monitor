const urlParams = new URLSearchParams(window.location.search);
let userUID = urlParams.get("UserID");

var livebutton = document.getElementById('livebutton');
livebutton.href = "./live_patient.html?UserID=" + userUID
var historybutton = document.getElementById('historybutton');
historybutton.href = "./patient_history.html?UserID=" + userUID

var temperaturevalue = document.getElementById('temperaturevalue');


firebase
  .database()
  .ref("/Patients")
  .once("value", function (snapshot) {
    let patientInfo = snapshot.val()[userUID]["patientInfo"];
    document.getElementById("patient_info").innerHTML += PatientHTMLGenerator(
      patientInfo
    );
  });

function PatientHTMLGenerator(patientinfo) {
  return `
    <img src="${patientinfo.imageURL}" class="profile_pic">
                    
    <div class="patient_id">
        <ul>
            <li id="patientname"></b>${patientinfo.Name}</li>
            <li><b>DOB: </b>${patientinfo.DOB}</li>
        </ul>
    </div>
    <div class="patient_status">
        <ul>
            <li><b>Abnormality detected: </b>${patientinfo.Abnormality}</li>
            <li><b>Condition: </b>${patientinfo.Condition} </li>
            <li><b>Contact Number: </b>028362391723 </li>
        </ul>
    </div>
    `;
}

var RefArray = [];
function initChart(id, title, primarycolor, yaxislabel) {
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
        borderWidth: 1
      }
    ]
  };
  chartConfig.labels = [];
  chartConfig.datasets[0].data = [];
  var ctx = document.getElementById(id).getContext("2d");
  var options = {
    maintainAspectRatio: false,
    animation: {
      duration: 0
    },
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
  if (RefArray[id].data.labels.length < 10) {
    RefArray[id].data.labels.push(label);
    RefArray[id].data.datasets.forEach(dataset => {
      dataset.data.push(value);
    });
  } else {
    RefArray[id].data.labels.shift(label);
    RefArray[id].data.datasets.forEach(dataset => {
      dataset.data.shift(value);
    });
  }
  // console.log(RefArray[id].data)
  RefArray[id].update();
}
function updateChartList(label, value, id,displaylength) {
  for (var index in value) {
    if (RefArray[id].data.datasets[0].data.length < displaylength) {
      RefArray[id].data.labels = [...Array(displaylength).keys()]
      RefArray[id].data.datasets.forEach(dataset => {
        dataset.data.push(...value);
      });
    } else {
      // RefArray[id].data.labels.shift(label + index);
      RefArray[id].data.datasets.forEach(dataset => {
        dataset.data.shift(...value);
      });

    }

  }

  RefArray[id].update();
}

function getChartData() {
  initChart("respChart", "Respiration Chart", "#3cd82c", "bpm");
  initChart("ecgChart", "ECG Chart", "#59eaed", "mV");
  initChart("ppgChart", "PPG Chart", "#f51a18", "ppg vals");
  var respref = firebase
    .database()
    .ref(userUID + "/respSensor");
  var ecgref = firebase
    .database()
    .ref(userUID + "/ecgSensor");
  var ppgref = firebase
    .database()
    .ref(userUID + "/ppgSensor");

  respref.limitToLast(500).once("value", function (snapshot) {
    try {
      var last500 = Object.values(snapshot.val()).slice(-500)
      updateChartList(1, last500, "tempChart", 50);
    } catch {
    }
    document.getElementsByClassName("loader")[0].style.display = "none";
    document.getElementsByClassName("chartContainer")[0].style.display = "flex";
    document.getElementsByClassName("livestats")[0].style.display = "flex";
  });
  ppgref.limitToLast(500).once("value", function (snapshot) {
    try{
      var last500 = Object.values(snapshot.val()).slice(-5).reduce((acc, val) => acc.concat(val))
      updateChartList(1, last500, "ppgChart", 125);
    } catch {}
  
  });
  ecgref.limitToLast(500).once("value", function (snapshot) {
    try{
      var last500 = Object.values(snapshot.val()).slice(-5).reduce((acc, val) => acc.concat(val))
      updateChartList(1, last500, "ecgChart", 125);
    } catch {}
  
  });
  respref.limitToLast(1).on("child_added", function (ret, prevChildKey) {
    updateChart(prevChildKey, ret.val(), "respChart");
  });
  ppgref.limitToLast(1).on("child_added", function (ret, prevChildKey) {
    updateChartList(prevChildKey, ret.val(), "ecgChart",500);
  });
  ecgref.limitToLast(1).on("child_added", function (ret, prevChildKey) {
    updateChartList(prevChildKey, ret.val(), "ppgChart",500);
  });
}
window.onload = getChartData();

