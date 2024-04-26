
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
import { getAuth ,GoogleAuthProvider,signInWithPopup} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
    
const firebaseConfig = {
    apiKey: "AIzaSyCOtJhN_j8WS_tutExFuQFpUNwYu73hCB0",
    authDomain: "hackathon-login-1f716.firebaseapp.com",
    projectId: "hackathon-login-1f716",
    storageBucket: "hackathon-login-1f716.appspot.com",
    messagingSenderId: "377282801492",
    appId: "1:377282801492:web:8e3b28e5253b3a197fa2c1",
    measurementId: "G-W6CMDMF51F"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const provider = new GoogleAuthProvider();
const auth = getAuth(app);
auth.languageCode = 'en'
const googleLogin = document.getElementById("google-login-btn");
googleLogin.addEventListener("click",function(){
    signInWithPopup(auth, provider)
  .then((result) => {
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const user = result.user;
    
    console.log(user);
    window.location.href = "../Templates/Hypredi.html"
  }).catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    const email = error.customData.email;
    const credential = GoogleAuthProvider.credentialFromError(error);
  });
})