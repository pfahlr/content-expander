import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';
import VerifyEmail from './components/VerifyEmail';
import ProfileForm from './components/ProfileForm';
import ResetPasswordForm from './components/ResetPasswordForm';
import ForgotPasswordForm from './components/ForgotPasswordForm';
import NavBar from './components/NavBar';
import LoginWithGoogleButton from './components/LoginWithGoogleButton';
import Logout from './components/Logout';
import { AuthProvider } from "./context/AuthContext";

export default function App() {
  return (
    <AuthProvider>
    <Router>
      <NavBar />
      <LoginWithGoogleButton />
      <Routes>
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/verify-email" element={<VerifyEmail />} />
        <Route path="/profile" element={<ProfileForm />} />
        <Route path="/forgot-password" element={<ForgotPasswordForm />} />
        <Route path="/reset-password" element={<ResetPasswordForm />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
    </Router>
    </AuthProvider>
  );
}
