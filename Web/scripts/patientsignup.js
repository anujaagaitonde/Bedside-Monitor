const patientname = document.getElementById("patientname").value;
const patientdob = document.getElementById("patientdob").value;
const patientcondition = document.getElementById("patientcondition").value;
const patientimageurl = document.getElementById("patientimageurl").value;
const patientcritical = document.getElementById("patientcritical").value;
const deviceid = document.getElementById("deviceid").value;

var database = firebase.database();

function addUser() {
    firebase.database().ref(deviceid + '/' + userId).set({
        abnormality: patientname,
        condition: patientcondition,
        critical: patientcritical,
        DOB: patientdob,
        Name: patientname,
        Starred: False,
        imageURL: patientimageurl
    });
}