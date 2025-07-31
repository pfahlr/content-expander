import React, { useEffect, useState } from 'react';
import axios from '../api/axiosInstance';
import Layout from '../components/Layout';
import { buttonClasses, inputClasses, formHeadingClasses, formContainerClasses, formClasses } from '../styles/classNames';

export default function ProfileForm() {
  const [profile, setProfile] = useState(null);
  const [msg, setMsg] = useState('');

  useEffect(() => {
    axios.get('/users/me')
      .then((res) => setProfile(res.data))
      .catch(() => setMsg('Failed to fetch profile.'));
  }, []);

  const handleSave = async (e) => {
    e.preventDefault();
    try {
      console.log(profile);
      await axios.patch('/users/me', profile);
      setMsg('Profile updated!');
    } catch (err) {
      setMsg('Update failed.');
    }
  };

  if (!profile) return <p>Loading...</p>;

  return (
    <Layout>
      <section className={formContainerClasses}>  
      <form onSubmit={handleSave} className={formClasses}>
      <h2 className={formHeadingClasses}>Profile</h2>
      email:
      <input className={inputClasses} value={profile.email} onChange={(e) => setProfile({ ...profile, email: e.target.value })} />
      phone:
      <input className={inputClasses} value={profile.phone} onChange={(e) => setProfile({ ...profile, phone: e.target.value })} />
      profile image:
      <input className={inputClasses} value={profile.profile_image} onChange={(e) => setProfile({ ...profile, profile_image: e.target.value })} />
      profile banner image:
      <input className={inputClasses} value={profile.profile_banner} onChange={(e) => setProfile({ ...profile, profile_banner: e.target.value })} />
      profile headline:
      <input className={inputClasses} value={profile.profile_headline} onChange={(e) => setProfile({ ...profile, profile_headline: e.target.value })} />
      display name:
      <input className={inputClasses} value={profile.profile_displayname} onChange={(e) => setProfile({ ...profile, profile_displayname: e.target.value })} />


      {/* Add more fields as needed */}

      <button className={buttonClasses} type="submit">Save</button>
      <p>{msg}</p>
      </form>
      </section>
    </Layout>
  );
}
