import React, { useState } from 'react';
import axios from '../api/axiosInstance';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

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
    <Layout>
    <section className={formContainerClasses}>
      <form onSubmit={handleSubmit} className={formClasses}>
      <h2 className={formHeadingClasses}>Reset Password</h2>
      <input className={inputClasses} type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <button className={buttonClasses} type="submit">Reset Password</button>
      <p>{msg}</p>
      </form>
      </section>
    </Layout>
  );
}
