// Initialize Firebase
config = {
  apiKey: "AIzaSyDFZ2WAZae-55_UK9KN_b9EbSAhhS-PTD8",
  authDomain: "bedsidemonitor.firebaseapp.com",
  databaseURL: "https://bedsidemonitor.firebaseio.com",
  projectId: "bedsidemonitor",
  storageBucket: "bedsidemonitor.appspot.com",
  messagingSenderId: "680750955239",
  appId: "1:680750955239:web:35f53ec6bc0227b6"
}
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
      .then(function() { window.location.replace("./all_patient_dashboard.html")})
      .catch(function(error) {
        window.alert(error.message);
      });
  }
}


