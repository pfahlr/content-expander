import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';
import VerifyEmail from './components/VerifyEmail';
import ProfileForm from './components/ProfileForm';
import NavBar from './components/NavBar';

export default function App() {
  return (
    <Router>
      <NavBar />

      <Routes>
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/verify-email" element={<VerifyEmail />} />
        <Route path="/profile" element={<ProfileForm />} />
      </Routes>
    </Router>
  );
}
