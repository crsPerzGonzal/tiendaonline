from fastapi import FastAPI, HTTPException
import mysql.connector
from backend.core.confi import get_connetion
from backend.models.user import User, regiUser,product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"hola" : "mundo"}

@app.post("/users")
async def login(user: User):
    connection = get_connetion()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
    
    try:
        cursor.execute(query, (user.username, user.password_hash))
        user_result = cursor.fetchone()
        
        if user_result:
            return user_result  # Devuelve la información del usuario
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o contraseña incorrecta.")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Error al conectar con MySQL: {err}')
    finally:
        cursor.close()
        connection.close()

@app.post("/insert")
async def new_cuent(resgistro: regiUser):
    connection = get_connetion()
    cursor = connection.cursor(dictionary=True)
    query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
    
    try:
        cursor.execute(query, (resgistro.username, resgistro.email, resgistro.password_hash))
        connection.commit()  # Confirma la inserción en la base de datos

        if cursor.rowcount > 0:
            return {"message": "Usuario insertado exitosamente", "username": resgistro.username}
        else:
            raise HTTPException(status_code=404, detail="Error al ingresar los datos")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Error al conectar con MySQL: {err}')
    finally:
        cursor.close()
        connection.close()


@app.get("/productos")  # Nota el plural aquí
async def get_productos():
    connection = get_connetion()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT product_id , name, price, image_url, description FROM products"

    try:
        cursor.execute(query)
        productos = cursor.fetchall()
        return productos  # Devuelve la lista de productos
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Error al conectar con MySQL: {err}')
    finally:
        cursor.close() # Este se queda... 
        #connection.close() esto no debe estar en este lugar, solo se termina el cursor. 




