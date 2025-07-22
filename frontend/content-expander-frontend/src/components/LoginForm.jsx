import React, { useState } from 'react';
import axios from '../api/axiosInstance';
import { useNavigate } from 'react-router-dom';
import qs from 'qs';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      var response = await axios.post('/auth/jwt/login',
          qs.stringify({username: email,password: password,}),
          {
            headers: {'Content-Type': 'application/x-www-form-urlencoded',},
          }
        );
      const token = response.data.access_token;
      console.log(response);
      sessionStorage.setItem('accessToken', token);
      setMsg('Login successful!');
      navigate('/profile');
    } 
    catch (err) {
      setMsg('Login failed.'+err);
      console.log(err)
    }
  };

  return (
    <Layout>
    <section className={formContainerClasses}>
      <h2 className={formHeadingClasses}>Login</h2>
      <form  className={formClasses} onSubmit={handleLogin}>
      <input className={inputClasses} value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
      <input className={inputClasses} type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <button className={buttonClasses} type="submit">Login</button>
      <p>{msg}</p>
      </form>
      <a href="/forgot-password">Forgot Password?</a>
    </section>
    </Layout>
  );
}
