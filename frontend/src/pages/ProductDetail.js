import React, { useEffect, useState, useContext } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { CartContext } from "../contexts/CartContext";
import "./ProductDetail.css"; // Crea un archivo CSS para estilos específicos

const ProductDetail = () => {
  const { product_id } = useParams(); // Obtener el ID del producto de la URL
  const [product, setProduct] = useState(null);
  const [error, setError] = useState(""); // Agregar estado para manejar errores
  const { addToCart } = useContext(CartContext);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        if (!product_id) {
          setError("ID de producto no válido.");
          return;
        }

        console.log("Obteniendo producto con ID:", product_id);

        const response = await axios.get(`http://127.0.0.1:8000/productos/${product_id}`);
        
        if (response.status === 200 && response.data) {
          setProduct(response.data);
          console.log("Producto recibido:", response.data);
        } else {
          setError("No se encontró el producto.");
        }
      } catch (error) {
        console.error("Error al obtener el producto:", error);
        setError("Hubo un problema al cargar el producto.");
      }
    };

    fetchProduct();
  }, [product_id]);

  if (error) return <p>{error}</p>;

  if (!product) return <p>Cargando producto...</p>;

  return (
    <div className="product-detail">
      <img src={product.image_url} alt={product.name} />
      <div className="detail-info">
        <h2>{product.name}</h2>
        <p>${product.price.toFixed(2)}</p>
        <p>{product.description}</p>
        <button onClick={() => addToCart(product)}>Añadir al Carrito</button>
      </div>
    </div>
  );
};

export default ProductDetail;