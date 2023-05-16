// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import firebase from "firebase/compat/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import firebaseui from "firebaseui";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA9kYFyk9zokwMD1okoiIlf3hk1sJa5jkc",
  authDomain: "weather-outfitter.firebaseapp.com",
  projectId: "weather-outfitter",
  storageBucket: "weather-outfitter.appspot.com",
  messagingSenderId: "233778568400",
  appId: "1:233778568400:web:801c6fc922f5c24f3952d5",
  measurementId: "G-W5DXYL1PSW"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
var ui = new firebaseui.auth.AuthUI(auth);

const uiConfig = {
  signInSuccessUrl: "/success",
  signInOptions: [
    {
      provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      // Additional OAuth scopes, if any
      scopes: ["https://www.googleapis.com/auth/contacts.readonly"],
      // Optional URL parameters
      customParameters: {
        // Prompt user to select account, even if there's only one
        prompt: "select_account",
      },
    },
    firebase.auth.EmailAuthProvider.PROVIDER_ID,
  ],
};

ui.start("#firebaseui-auth-container", uiConfig);
