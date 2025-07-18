import React, { useState } from 'react';
import axios from '../api/axiosInstance';

export default function ForgotPasswordForm() {
  const [email, setEmail] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/auth/forgot-password', { "email":email});
      setMsg('Check your email for link to reset your password.');
    } catch (err) {
      setMsg('Account not found.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Forgot Password</h2>
      <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <button type="submit">Send Password Reset Link</button>
      <p>{msg}</p>
    </form>
  );
}
