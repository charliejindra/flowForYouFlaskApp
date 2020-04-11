var database = firebase.database();

var firebaseConfig = {
  apiKey: "AIzaSyCrA1YkQJU9lf1tunCNYayg67QKhOQXEok",
  authDomain: "flowforyou-82126.firebaseapp.com",
  databaseURL: "https://flowforyou-82126.firebaseio.com",
  projectId: "flowforyou-82126",
  storageBucket: "flowforyou-82126.appspot.com",
  messagingSenderId: "464936460609",
  appId: "1:464936460609:web:f0c0b73b51ee20498001c0"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
console.log(firebase);

var ref = database.ref('dispensers/locations/Student Wellness Center/Restrooms');
var restroom = "Lower Level Restroom";
var data = {
    Mens: restroom,
    Womens: restroom
}
ref.push(data);
