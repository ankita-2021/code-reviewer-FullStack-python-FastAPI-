import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  // already logged in user redirect
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      navigate("/review");
    }
  }, []);

  const handleLogin = async () => {
    if (!email || !password) {
      alert("Email aur password daal pehle...");
      return;
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/login", {
        email,
        password,
      });

      // ✅ TOKEN SAVE
      localStorage.setItem("token", res.data.access_token);

      // ✅ REDIRECT
      navigate("/review");
    } catch (err) {
      if (err.response?.data?.error) {
        alert(err.response.data.error); // backend message show karega
      } else {
        alert("Login failed ❌");
      }
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-r from-indigo-500 to-purple-600">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-96">
        <h2 className="text-2xl font-bold text-center mb-6">Login</h2>

        <input
          className="w-full mb-3 p-2 border rounded-lg"
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="w-full mb-4 p-2 border rounded-lg"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-indigo-600 text-white p-2 rounded-lg hover:bg-indigo-700 transition transform hover:scale-105"
        >
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;
