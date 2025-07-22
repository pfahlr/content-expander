// src/context/AuthContext.jsx
import { createContext, useContext, useEffect, useState } from "react";
import axios from '../api/axiosInstance';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // user object from backend
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    axios.get('/users/me')
      .then((res) => {console.log(res.data); setUser(res.data)}).then(setLoading(false))
      .catch(() => console.log('error'));
    }, []);

  return (
    <AuthContext.Provider value={{ user, setUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
