
importScripts('https://www.gstatic.com/firebasejs/8.3.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.3.1/firebase-messaging.js');


  var firebaseConfig = {
    apiKey: "AIzaSyBXBYaToCdIQOkVHPuBzO2VWimr-jh2yrg",
    authDomain: "kampus-52a9f.firebaseapp.com",
    projectId: "kampus-52a9f",
    storageBucket: "kampus-52a9f.appspot.com",
    messagingSenderId: "576665983294",
    appId: "1:576665983294:web:25c4323279412c349af46f",
    measurementId: "G-5X0VH0R9GV"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
const messaging=firebase.messaging();
messaging.usePublicVapidKey('BA515hrbYgT-oqfRhCon0CJIyjzU_ivliKX6Q9G93dhIGVXZfK9KkI2pT-lvmd-ZFmGTKv_2UkuoDlM-ZFlk0vk');

messaging.onBackgroundMessage(function(payload) {
console.log('[firebase-messaging-sw.js] Received background message ', payload);
var obj = payload.notification;
// Customize notification here
var notificationTitle = obj.title;
var notificationOptions = {
body: obj.body,
icon: 'static/images/logo.png',
tag: "notification-1"

};
return self.registration.showNotification(notificationTitle,notificationOptions);
});


