import React, { useEffect, useState } from 'react';
import axios from '../api/axiosInstance';

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
      await axios.patch('/users/me', profile);
      setMsg('Profile updated!');
    } catch (err) {
      setMsg('Update failed.');
    }
  };

  if (!profile) return <p>Loading...</p>;

  return (
    <form onSubmit={handleSave}>
      <h2>Profile</h2>
      <input value={profile.email} onChange={(e) => setProfile({ ...profile, email: e.target.value })} />
      {/* Add more fields as needed */}
      <button type="submit">Save</button>
      <p>{msg}</p>
    </form>
  );
}
