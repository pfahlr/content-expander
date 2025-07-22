import React, { useState } from 'react';
import axios from '../api/axiosInstance';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

export default function RegisterForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/auth/register', { "email":email, "password":password });
      setMsg('Registered successfully! Check your email to verify.');
    } catch (err) {
      setMsg('Registration failed.');
    }
  };

  return (
    <Layout>
      <section className={formContainerClasses}>
      <h2 className={formHeadingClasses}>Create an Account</h2>
      <form className={formClasses} onSubmit={handleSubmit}>
      <input className={inputClasses}  value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <input className={inputClasses}  type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <button className={buttonClasses} type="submit">Register</button>
      <p>{msg}</p>
      </form>
      </section>
    </Layout>
  );
}
