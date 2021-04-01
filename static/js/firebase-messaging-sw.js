
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

messaging.setBackgroundMessageHandler(function (payload) {
    console.log(payload);
    const notification=JSON.parse(payload);
    const notificationOption={
        body:notification.body,
        icon:notification.icon
    };
    return self.registration.showNotification(payload.notification.title,notificationOption);
});
