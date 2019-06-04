

activetab = "patientlistall"


function generateHTML(patientInfo, userID) {
  return `
<div class="patient_block" id="patient">
  <div class="profpicwrap">
    <img src="${patientInfo.imageURL}" class="profile_pic">
  </div>
  <div class="patient_id">
    <ul>
      <li><b>Name: </b>${patientInfo.Name}</li>
      <li><b>DOB: </b>${patientInfo.DOB}</li>
    </ul>
    <p id="demo"></p>
  </div>
  <div class="patient_status">
    <ul>
      <li><b>Abnormality detected: </b>${patientInfo.Abnormality}</li>
      <li><b>Condition: </b>${patientInfo.Condition} </li>
      <li><b>Connection status: </b>XXX</li>
    </ul>
  </div>
  <!-- only top star changes - check-->
  <div id="starwrap">
    <div id="star${userID}" class=${(patientInfo.Starred ? "starred" : "unstarred")} onclick="toggleStar(this.id)"></div>
  </div>
  <div id="viewbtnwrap">
    <div class = "view_btn"><a href="live_patient.html?UserID=${userID}">VIEW</a></div>
  </div>
</div>
 `
}

function addPatientHTML() {
  return `
    <div class="plusbuttonwrapper">
      <img src="images/plus.png" class="plusbutton" onclick="location.href = './new_patient.html'">
    </div>
  `
}

let ref = firebase.database().ref("/")
let listref = document.getElementsByClassName("patientlist")[0]
listtype = listref.id

patients = {};

//function run on page load
(function () {
  ref.once("value", function (snapshot) {
    listref.innerHTML = ""

    for (var userID in snapshot.val()) {
      let patientInfo = snapshot.val()[userID]['patientInfo']
      patients[userID] = patientInfo
    }
    document.getElementsByClassName("loader")[0].style.display = "none";
    showTab(null, "patientlistall")
  }, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
  });
})();


ref.on("value", function (snapshot) {
  listref.innerHTML = ""
  for (var userID in snapshot.val()) {
    let patientInfo = snapshot.val()[userID]['patientInfo']
    patients[userID] = patientInfo
  }
  showTab(null, activetab)
}, function (errorObject) {
  console.log("The read failed: " + errorObject.code);
});


function showTab(evt, patienttype) {
  activetab = patienttype;
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("patientlist");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("link_button");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  currenttab = document.getElementById(patienttype)
  currenttab.style.display = "flex";

  if (patienttype == "patientlistcritical") {
    currenttab.innerHTML = "";
    for (var userID in Object.keys(patients)) {
      if (Object.values(patients)[userID].Critical) {
        currenttab.innerHTML += generateHTML(Object.values(patients)[userID], Object.keys(patients)[userID]);
      }
    }
  } else if (patienttype == "patientliststarred") {
    currenttab.innerHTML = "";
    for (var userID in Object.keys(patients)) {
      if (Object.values(patients)[userID].Starred) {
        currenttab.innerHTML += generateHTML(Object.values(patients)[userID], Object.keys(patients)[userID]);
      }
    }
  } else {
    currenttab.innerHTML = "";
    for (var userID in Object.keys(patients)) {
      currenttab.innerHTML += generateHTML(Object.values(patients)[userID], Object.keys(patients)[userID]);
    }
  }
  try {
    evt.currentTarget.className += " active";
  } catch{

  }
}