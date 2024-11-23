// src/components/Cart.js
import React, { useContext, useState } from "react";
import { CartContext } from "../contexts/CartContext";
import axios from "axios"; // Importa Axios
import "./Cart.css"; // Crea un archivo CSS para estilos específicos

const Cart = () => {
  const { cartItems, removeFromCart, clearCart } = useContext(CartContext);
  const [showCheckout, setShowCheckout] = useState(false);
  const [username, setUsername] = useState("");
  const [password_hash, setPassword] = useState("");

  const totalPrice = cartItems.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  const handleCheckout = async (e) => {
    e.preventDefault();

    try {
      // Autenticación del usuario
      const response = await axios.post("http://127.0.0.1:8000/api/users", {
        username,
        password_hash,
      });
      console.log("captura el id", response.data)
      const user_id = response.data.user_id; // Asegúrate de que la respuesta contenga el user_id
      console.log("capture el idxx", user_id)
      const orderData = {
        user_id,
        order_date: new Date().toISOString(), // Asegúrate de que esto esté en el formato correcto
        status: "pending", // Asegúrate de que esto sea un valor válido para tu Enum
        total_amount: totalPrice, // Usa el total calculado
    };
      // Crear la orden
     
      

      const orderResponse = await axios.post("http://127.0.0.1:8000/api/inset_orden/", orderData);

      console.log("Orden creada:", orderResponse.data);

      // Limpia el carrito después de procesar la compra
      clearCart();
      setShowCheckout(false); // Oculta el formulario de checkout
    } catch (error) {
      console.error("Error:", error);
      // Aquí puedes agregar lógica para mostrar un mensaje de error al usuario
    }
  };

  return (
    <div className="cart-container">
      <h2>Carrito de Compras</h2>
      {cartItems.length === 0 ? (
        <p>Tu carrito está vacío.</p>
      ) : (
        <div>
          <ul>
            {cartItems.map((item) => (
              <li key={item.product_id} className="cart-item">
                <img src={item.image_url} alt={item.name} />
                <div className="item-details">
                  <h4>{item.name}</h4>
                  <p>Precio: ${item.price.toFixed(2)}</p>
                  <p>Cantidad: {item.quantity}</p>
                  <button onClick={() => removeFromCart(item.product_id)}>
                    Eliminar
                  </button>
                </div>
              </li>
            ))}
          </ul>
          <div className="cart-summary">
            <h3>Total: ${totalPrice.toFixed(2)}</h3>
            <button onClick={clearCart}>Limpiar Carrito</button>
            <button onClick={() => setShowCheckout(true)}>Finalizar Compra</button>
          </div>
        </div>
      )}
      {showCheckout && (
        <div className="checkout-form">
          <h3>Finalizar Compra</h3>
          <form onSubmit={handleCheckout}>
            <div>
              <label>Nombre de Usuario:</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div>
              <label>Contraseña:</label>
              <input
                type="password"
                value={password_hash}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit">Confirmar Compra</button>
            <button type="button" onClick={() => setShowCheckout(false)}>
              Cancelar
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default Cart;