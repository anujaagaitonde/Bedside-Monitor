// Initialize Firebase
var config = {
  apiKey: "AIzaSyB3OD82TJeIDHOwiys2Cy_iD8wj5KxBvwU",
  authDomain: "mfbedside.firebaseapp.com",
  databaseURL: "https://mfbedside.firebaseio.com",
  projectId: "mfbedside",
  storageBucket: "mfbedside.appspot.com",
  messagingSenderId: "477689150813",
  appId: "1:477689150813:web:3e2c87dc310d4576"
};
firebase.initializeApp(config);

//Get elements

const auth = firebase.auth();

//Add login Click event
function loginUser() {
  const btnLogin = document.getElementById("login_submit");
  const email = document.getElementById("EmailInput").value;
  const pass = document.getElementById("PasswordInput").value;
  //Sign in
  auth
    .signInWithEmailAndPassword(email, pass)
    .then(e => window.location.replace("./all_patient_dashboard.html"))
    .catch(e => window.alert(e));
}
function logoutUser() {
  const btnLogout = document.getElementById("logout");
  firebase
    .auth()
    .signOut()
    .then(function() {
      window.location.replace("./login.html");
    })
    .catch(function(error) {
      console.log(error);
    });
}

function createUser() {
  const doctorname = document.getElementById("doctorname").value;
  const doctoremail = document.getElementById("doctoremail").value;
  const doctorpass = document.getElementById("doctorpass").value;
  const doctorpassconfirm = document.getElementById("doctorpassconfirm").value;

  if (doctorpass != doctorpassconfirm) {
    window.alert("The entered passwords do not match");
  } else {
    auth
      .createUserWithEmailAndPassword(doctoremail, doctorpass)
      .signInWithEmailAndPassword(doctoremail, doctorpass)
      .then(function() { window.location.replace("./critical_patient_dashboard.html")})
      .catch(function(error) {
        window.alert(error.message);
      });
  }
}


