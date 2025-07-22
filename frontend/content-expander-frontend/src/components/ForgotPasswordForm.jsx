import React, { useState } from 'react';
import axios from '../api/axiosInstance';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

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
    <Layout>
    <section className={formContainerClasses}>
      <h2 className={formHeadingClasses}>Forgot Password</h2>
      <form onSubmit={handleSubmit} className={formClasses}>
      <input className={inputClasses} value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <button className={buttonClasses} type="submit">Send Password Reset Link</button>
      <p>{msg}</p>
      </form>
    </section>
    </Layout>
  );
}
