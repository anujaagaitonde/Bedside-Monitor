var config = {
    apiKey: "AIzaSyB6mXwNEirNupF2wT28lclPJ9YjvFe1eQo",
    authDomain: "mfmonitor-80a0d.firebaseapp.com",
    databaseURL: "https://mfmonitor-80a0d.firebaseio.com",
    projectId: "mfmonitor-80a0d",
    storageBucket: "mfmonitor-80a0d.appspot.com",
    messagingSenderId: "171419436747",
    appId: "1:171419436747:web:e45ee688cbb5c5f0"
};
firebase.initializeApp(config);

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
                <div id="star" class="unstarred" onclick="toggleStar()"></div>
                <div class = "view_btn"><a href="live_patient.html">VIEW</a></div>
            </div>
            `
}
let ref = firebase.database().ref("/")
ref.on("value", function (snapshot) {
    for (var userID in snapshot.val()) {
        let patientInfo = snapshot.val()[userID]['patientInfo']
        document.getElementById("patientlist").innerHTML += generateHTML(patientInfo, userID);
    }
}, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
});