import React, { useEffect, useState } from 'react';
import axios from '../api/axiosInstance';
import { useLocation, useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

export default function VerifyEmail() {
  const location = useLocation();
  const navigate = useNavigate();
  const [msg, setMsg] = useState('');

  useEffect(() => {
    const token = new URLSearchParams(location.search).get('token');
    if (token) {
      axios.post('/auth/verify', { token })
        .then(() => {
          setMsg('Email verified! You can now log in.');
          setTimeout(() => navigate('/login'), 2000);
        })
        .catch(() => setMsg('Verification failed.'));
    } else {
      setMsg('No token found.');
    }
  }, [location]);

  return (
    <div>
      <h2>Email Verification</h2>
      <p>{msg}</p>
    </div>
  );
}
