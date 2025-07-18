import React from 'react';
import { Link } from 'react-router-dom';



const GOOGLE_LOGIN_URL = "http://localhost:8000/auth/google/login";
export default function LoginWithGoogleButton() {
  return (
    <a href={GOOGLE_LOGIN_URL}>
      <button>Login with Google</button>
    </a>
  );
}