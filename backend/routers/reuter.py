from fastapi import APIRouter
from fastapi import Depends , HTTPException
from backend import Crud as crud
from backend.core.confi import get_db
from sqlalchemy.orm import Session
from backend.schemas.response import UserSchema, Response, RegiSchema

router = APIRouter()


@router.post('/users')
async def create_user_name(request:UserSchema, db:Session = Depends(get_db)):
    try:
        user = await crud.login(db, users=request)
        return {
            "status": "ok",
            "code": "200",
            "message": "usuario creado",
            "result": user
        }
    except HTTPException as http_err:
        raise http_err
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {err}")
    

@router.post('/create')
async def create_regi(request:RegiSchema, db:Session = Depends(get_db)):
    try:
        # Llama a la función CRUD para crear el usuario
        new_usuario = create_regi(db, regiUser=request)
        return {
            "status": "ok",
            "code": 200,
            "message": "Usuario creado exitosamente",
            "result": {
                "id": new_usuario.id,
                "username": new_usuario.username,
                "email": new_usuario.email
            }
        }
    except HTTPException as http_err:
        # Reenvía los errores definidos
        raise http_err
    except Exception as err:
        # Captura errores inesperados
        raise HTTPException(status_code=500, detail=f"Error interno: {err}")