
importScripts('https://www.gstatic.com/firebasejs/8.3.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.3.1/firebase-messaging.js');


  var firebaseConfig = {
    apiKey: "AIzaSyDrZRgm_9-xauyre5flvN_KxLLYqQ8MCv0",
    authDomain: "kampus-305500.firebaseapp.com",
    projectId: "kampus-305500",
    storageBucket: "kampus-305500.appspot.com",
    messagingSenderId: "968358554586",
    appId: "1:968358554586:web:f22fed2afe90864b5d6ee3",
    measurementId: "G-5FE0JQ1XEE"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
const messaging=firebase.messaging();
messaging.usePublicVapidKey('BMc_Wye4mGlB5K76dN8Mdnt-4Fi-VyjjRzFpOdvlzuG8yelcS_HWNiCpjTLVRVkfunPIWYbCYRQwaHs0AJCRGNc');

messaging.onBackgroundMessage(function(payload) {
console.log('[firebase-messaging-sw.js] Received background message ', payload);
var obj = payload.notification;
// Customize notification here
var notificationTitle = obj.title;
var notificationOptions = {
body: obj.body,
icon: 'static/images/logo.png',
};
return self.registration.showNotification(notificationTitle,notificationOptions);
});


