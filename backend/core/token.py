from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from fastapi import Request, HTTPException
from backend.core.confi import SessionLocal
from backend.models.user import Users
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY') or "default_secret_key"  
ALGORITHM = os.getenv('ALGORITHM') or "HS256"
TOKEN_EXPIRE_MINUTES = int(os.getenv('TOKEN_EXPIRE_MINUTES', 30))


def create_token(password_hash: str):
    try:
        expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
        payload = {
            "password_hash": password_hash,
            "exp": expiration
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        print("[DEBUG] Token generado:", token)
        return token
    except Exception as e:
        print("[ERROR] Error generando el token:", str(e))
        raise HTTPException(status_code=500, detail="Error interno al generar el token.")


def verify_token(token: str):
    try:
        print("[DEBUG] Decodificando token:", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("[DEBUG] Payload decodificado:", payload)

        password_hash = payload.get("password_hash")
        if not password_hash:
            print("[ERROR] Token inválido: falta 'password_hash'")
            raise HTTPException(status_code=403, detail="Token inválido: falta 'password_hash'.")

        print("[DEBUG] Verificando usuario en la base de datos...")
        session = SessionLocal()
        user = session.query(Users).filter(Users.password_hash == password_hash).first()
        if not user:
            print("[ERROR] Usuario no encontrado para password_hash:", password_hash)
            raise HTTPException(status_code=403, detail="Token inválido: usuario no autorizado.")

        print("[DEBUG] Token válido para usuario:", user.user_id)
        return payload

    except JWTError as jwt_error:
        print("[ERROR] Error al decodificar el token JWT:", str(jwt_error))
        raise HTTPException(status_code=403, detail="Token inválido o expirado.")

    except Exception as e:
        print("[ERROR] Error inesperado al verificar token:", str(e))
        raise HTTPException(status_code=500, detail="Error interno al verificar el token.")


class MyHTTPBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(MyHTTPBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """Valida las credenciales en el encabezado de autorización."""
        try:
            credentials: HTTPAuthorizationCredentials = await super(MyHTTPBearer, self).__call__(request)

            if not credentials:
                print("[ERROR] No se proporcionaron credenciales.")
                raise HTTPException(status_code=403, detail="No se proporcionaron credenciales.")

            if credentials.scheme != "Bearer":
                print("[ERROR] Esquema de autenticación inválido:", credentials.scheme)
                raise HTTPException(status_code=403, detail="Esquema de autenticación inválido.")

            print("[DEBUG] Verificando token con esquema Bearer...")
            payload = verify_token(credentials.credentials)
            return payload

        except HTTPException as e:
            print("[ERROR] HTTPException durante la validación del token:", e.detail)
            raise e

        except Exception as e:
            print("[ERROR] Error inesperado en MyHTTPBearer:", str(e))
            raise HTTPException(status_code=500, detail="Error interno durante la autenticación.")