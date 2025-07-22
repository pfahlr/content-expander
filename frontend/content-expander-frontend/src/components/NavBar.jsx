// components/NavBar.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from "../context/AuthContext";

export default function NavBar() {
  const { user, loading } = useAuth();
  if (loading) return null;
  return (
    <nav>
      <ul>
        {!user && (
        <>
        <li><Link to="/register">Register</Link></li>
        <li><Link to="/login">Login</Link></li>
        </>
        )}
        {user && (
        <>
        <li><Link to="/profile">Profile</Link></li>
        <li><Link to="/logout">Logout</Link></li>
        </>
        )}
      </ul>
    </nav>
  );
}
