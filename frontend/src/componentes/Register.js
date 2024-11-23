// src/components/Register.js
import React, { useState } from "react";
import axios from "axios";
import "./Auth.css"; // Reutiliza estilos de Login

const Register = () => {
  const [username, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password_hash, setPassword] = useState("");
  const [userRegistreLook, setuserRegistreLook] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    // Aquí agregarás la lógica para registrar al usuario
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/create", {
        username,
        email,
        password_hash,
      });
      console.log(response.data);
      if (response.data)
        setuserRegistreLook(response.data.username);
      else {
        alert("error de insertar datos") 
      }

      }catch (error) {
      console.error("Error al registrar", error);
    }
  };

  return (
    <div className="auth-container">
    <h2>{userRegistreLook ? `registro exitoso, ${userRegistreLook}!`: "iniciar seccion"}</h2> {}
      {userRegistreLook ? (
        null
      ) : (
      <form onSubmit={handleRegister}>
        <div className="form-group">
          <label>Nombre</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Correo Electrónico</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Contraseña</label>
          <input
            type="password"
            value={password_hash}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Registrar</button>
      </form>
      )}
    </div>
  );
};

export default Register;
