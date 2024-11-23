<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>
    <h1>tienda online</h1>
    <p><em>(tienda de venta de ropa de toda clase,  articulos y variedad)</em></p>

    <h2>Descripción</h2>
    <p><em>("Este proyecto tiene como objetivo gestionar las órdenes de compra y ventas de una tienda en línea mediante una API robusta y escalable.")</em></p>

    <h2>Instalación y Ejecución</h2>
    <p>1paso: activa tu entorno y prende uvicorn usando uvicorn main:app --reload --host 127.0.0.1 --port 8000, segundo crea un segunda termainal activas en entorno y te mueves a la capeta front (cd front) y usa el npm start y tener prendido el un localhost y una base de datos proporcionada por el repositori</p>

    <h3>Prerrequisitos</h3>
    <ul>
        <li><strong>Python 3.9 o superior</strong></li>
        <li><strong>Node.js</strong> (si incluye frontend)</li>
        <li><strong>MySQL</strong> o cualquier base de datos compatible configurada</li>
    </ul>

    <h3>Instrucciones</h3>
    <ol>
        <li>Clona este repositorio:
            <pre><code>https://github.com/crsPerzGonzal/tiendaonline</code></pre>
        </li>
        <li>Ve al directorio del proyecto:
            <pre><code>https://github.com/crsPerzGonzal/tiendaonline</code></pre>
        </li>
        <li>Configura un entorno virtual (opcional pero recomendado):
            <pre><code>python -m venv env<br>
source env/bin/activate  # En Windows: env\Scripts\activate</code></pre>
        </li>
        <li>Instala las dependencias:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Configura el archivo <code>.env</code> con las variables necesarias:
            <pre><code>DATABASE_URL=mysql+mysqlconnector://user:password@localhost:3306/database_name<br>
SECRET_KEY=your_secret_key</code></pre>
        </li>
        <li>Realiza las migraciones de la base de datos:
            <pre><code>alembic upgrade head</code></pre>
        </li>
        <li>Ejecuta el servidor:
            <pre><code>uvicorn main:app --reload</code></pre>
        </li>
    </ol>

    <h3>Opcional (Frontend)</h3>
    <p><em>(Si aplica, describe cómo ejecutar el frontend aquí, como instalar dependencias con <code>npm install</code> y ejecutar con <code>npm start</code>.)</em></p>

    <h2>Tecnologías Utilizadas</h2>
    <ul>
        <li><strong>FastAPI</strong>: Framework backend para crear APIs rápidas y modernas.</li>
        <li><strong>SQLAlchemy</strong>: ORM para gestionar la base de datos.</li>
        <li><strong>MySQL</strong>: Base de datos relacional.</li>
        <li><strong>Pydantic</strong>: Validación de datos y serialización.</li>
        <li><em>(Agrega otras tecnologías que uses, como React, Docker, etc.)</em></li>
    </ul>

    <h2>Detalles del Grupo</h2>
    <ul>
        <li><strong>cristian perez gonzalez</strong>: Líder del proyecto, desarrollador backend.</li>
        <li><strong>andres pedroza</strong>: Desarrolladora frontend.</li>
        <li><strong> yimileth manga</strong>: Especialista en base de datos.</li>
        <li><strong>  jordy andres</strong>:crador de recursos.</li>
    </ul>

    <h2>Enlaces de Despliegue</h2>
    <p><em></em></p>
    <ul>
    </ul>
</body>
</html>

