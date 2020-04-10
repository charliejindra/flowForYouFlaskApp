import Firebase from 'firebase';
var dataRef = new Firebase('firebase url');
console.log("Firebase : "+Firebase+" -- dataRef :: "+dataRef)
dataRef.set("Firebase Require");


  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyCrA1YkQJU9lf1tunCNYayg67QKhOQXEok",
    authDomain: "flowforyou-82126.firebaseapp.com",
    databaseURL: "https://floxzwforyou-82126.firebaseio.com",
    projectId: "flowforyou-82126",
    storageBucket: "flowforyou-82126.appspot.com",
    messagingSenderId: "464936460609",
    appId: "1:464936460609:web:f0c0b73b51ee20498001c0"
  };
  const firebase = require("firebase");
  firebase.on('ready', () => {
    mainWindow = new BrowserWindow({
        webPreferences: {
            nodeIntegration: false
        }
    });
});
// Required for side-effects


// Initialize Cloud Firestore through Firebase
firebase.initializeApp({
  apiKey: "AIzaSyCrA1YkQJU9lf1tunCNYayg67QKhOQXEok",
  authDomain: "flowforyou-82126.firebaseapp.com",
  projectId: "flowforyou-82126"
});




var db = firebase.database();
var building;
var floor;
//var locationID = "3uMc77sMjH97Yh8cnMiU";
building = "Bowman Hall";
var location = "Second Floor RestRoom";
var mens;
var universal;




function writeUserData(projectId, building, mens, universal) {
  firebase.database().ref('locations/' + '3uMc77sMjH97Yh8cnMiU/' + 'Bowman Hall' + 'TJoOi3fGF1OSk2Ge2z2d'.set({
    mens: location
  }));
}

