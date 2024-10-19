import React, { createContext, useState } from "react";

// Crear el contexto
export const CartContext = createContext();

// Proveedor del contexto
export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);

  // Añadir producto al carrito
  const addToCart = (product) => {
    setCartItems((prevItems) => {
      const itemExists = prevItems.find((item) => item.product_id === product.product_id);
      if (itemExists) {
        // Incrementar la cantidad si el producto ya existe
        
        return prevItems.map((item) =>
          item.product_id === product.product_id
            ? { ...item, quantity: item.quantity + 1 }
            : item
            
        );
        
      } else {
        
        // Añadir el producto con cantidad 1
        return [...prevItems, { ...product, quantity: 1 }];
        
      }
    });
  };

  // Eliminar producto del carrito
  const removeFromCart = (productId) => {
    console.log("Eliminando producto con ID:", productId);
    setCartItems((prevItems) =>
      prevItems.filter((item) => item.product_id !== productId)
    );
  };

  // Limpiar todo el carrito
  const clearCart = () => {
    console.log("Limpiando el carrito...");
    setCartItems([]);
  };

  return (
    <CartContext.Provider
      value={{ cartItems, addToCart, removeFromCart, clearCart }}
    >
      {children}
    </CartContext.Provider>
  );
};