// src/components/ProductItem.js
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { CartContext } from "../contexts/CartContext";
import "./ProductItem.css"; // Crea un archivo CSS para estilos específicos

const ProductItem = ({ product }) => {
  const { addToCart } = useContext(CartContext);
  const handleAddToCart = (product) => {
    console.log("Producto añadido al carrito:", product);
    addToCart(product);
  };
  return (
    <div className="product-item">
      <img src={product.image_url} alt={product.name} />
      <h3>{product.name}</h3>
      <p>${product.price.toFixed(2)}</p>
      <p>{product.description}</p>
      <div className="buttons">
      <button onClick={() => {
        console.log("Producto añadido:", product); // Aquí se registra el producto en la consola
        handleAddToCart(product); // Llama a la función para añadir al carrito
      }}>
        Añadir al Carrito
        </button>
        <Link to={`/products/${product.product_id}`}>
        <button>Ver Producto</button>
        </Link>
      </div>
    </div>
  );
};

export default ProductItem;
