// Initialize Firebase
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


