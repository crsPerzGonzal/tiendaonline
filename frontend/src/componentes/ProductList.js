import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import ProductItem from "./ProductItem";
import "./ProductList.css";

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Simulando la obtención de productos
    const fetchProducts = async () => { 
      try {
        // Reemplaza con tu ruta de API real
        const response = await axios.get("http://127.0.0.1:8000/api/producto");
        if (response.data) {
          setProducts(response.data); 
          console.log("producto mostrado" + response.data);
        } else {
          alert("error de insertar datos")
        }

      } catch (error) {
        console.error("Error al obtener productos", error);
      }
    };

    fetchProducts();
  }, []);

  // Si no tienes una API lista, puedes simular los productos:

  return (
    <div className="product-list">
      {products.length === 0 ? (
        <p>Cargando productos...</p>
      ) : (
        products.map((product) => (
          <ProductItem key={product.product_id} product={product} />
        ))
      )}
    </div>
  );
};

export default ProductList;
