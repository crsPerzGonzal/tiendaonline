// src/components/Login.js
import React, { useState } from "react";
import axios from "axios";
import "./Auth.css"; // Crea un archivo CSS para estilos específicos

const Login = () => {

  const [username, setUsername] = useState("");
  const [password_hash, setPasswordHash] = useState("");
  const [userNameDisplay, setUserNameDisplay] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    // Aquí agregarás la lógica para autenticar al usuario
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/users", { username, password_hash });
      if (response.data) {
        console.log("producto mostrado" + response.data);
        setUserNameDisplay(response.data.username);
      } else {
        alert("error de insertar datos")
      }

      // Manejar el inicio de sesión exitoso (por ejemplo, guardar el token)
    
    } catch (error) {
      console.error("Error al iniciar sesión", error);
    }
  };

  return (
    <div className="auth-container">
    <h2>{userNameDisplay ? `Bienvenido, ${userNameDisplay}!` : "Iniciar Sesión"}</h2> {/* Cambia el encabezado aquí */}
    {userNameDisplay ? ( // Condicional para mostrar el formulario o nada
      null // No se muestra el formulario si el usuario ha iniciado sesión
    ) : (
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label>Usuario</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Contraseña</label>
          <input
            type="password"
            value={password_hash}
            onChange={(e) => setPasswordHash(e.target.value)}
            required
          />
        </div>
        <button id="btnEntrar" type="submit">Ingresar</button>
      </form>
    )}
  </div>
);
};


export default Login;
