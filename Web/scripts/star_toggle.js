function toggleStar(starID) {
  userID = starID.replace('star','');
  console.log(userID)

    if (document.getElementById(starID).classList.contains("unstarred"))
    {
        document.getElementById(starID).classList.remove("unstarred");
        document.getElementById(starID).classList.add("starred");
        firebase.database().ref('/' + userID+'/patientInfo/').update({
          Starred:true
        })
    }
    else
    {
        document.getElementById(starID).classList.remove("starred");
        document.getElementById(starID).classList.add("unstarred");
        firebase.database().ref('/' + userID+'/patientInfo/').update({
          Starred:false
        })
    }

    return;
}
