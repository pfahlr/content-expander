import React, { useState } from 'react';
import axios from '../api/axiosInstance';

export default function ResetPasswordForm() {
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const token = new URLSearchParams(location.search).get('token');
    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        await axios.post('/auth/reset-password', { "password":password, "token":token});
        setMsg('Password Reset.');
      } catch (err) {
        setMsg('Error resetting password.');
      }
    };
  
  return (
    <form onSubmit={handleSubmit}>
      <h2>Forgot Password</h2>
    
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <button type="submit">Reset Password</button>
      <p>{msg}</p>
    </form>
  );
}
