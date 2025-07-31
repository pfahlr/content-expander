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
    axios.post('/auth/jwt/logout')
      .then(() => {
        setMsg('Logout Successful!');
        setTimeout(() => navigate('/login'), 2000);
      })
      .catch(() => setMsg('Logout failed.'));
  }, [location]);

  return (
    <Layout>
    <section className={formContainerClasses}>
      <h2 className={formHeadingClasses}>{msg}</h2>
    </section>
    </Layout>
  );
}
