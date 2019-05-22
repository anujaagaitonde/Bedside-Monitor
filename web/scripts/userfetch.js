

function validPatientFilter(listtype,patientInfo){
  if ((listtype=="patientlistcritical")&&!patientInfo.Critical){
    return false;
  } else if ((listtype=="patientliststarred")&&!patientInfo.Starred){
    return false;
  }
  return true;

}

function generateHTML(patientInfo, userID) {
    return `
<div class="patient_block" id="patient">
  <img src="images/profile_pic.png" class="profile_pic">
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
  <div id="star${userID}" class=${(patientInfo.Starred ? "starred" : "unstarred")} onclick="toggleStar(this.id)"></div>
  <div class = "view_btn"><a href="live_patient.html?UserID=${userID}">VIEW</a></div>
</div>
 `
}

let ref = firebase.database().ref("/")
let listref = document.getElementsByClassName("patientlist")[0]
listtype = listref.id

ref.on("value", function (snapshot) {
  listref.innerHTML = ""
    for (var userID in snapshot.val()) {
        let patientInfo = snapshot.val()[userID]['patientInfo']
        if (validPatientFilter(listref.id,patientInfo)){
          listref.innerHTML += generateHTML(patientInfo, userID);
        }
    }
}, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
});
