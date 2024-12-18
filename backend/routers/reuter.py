from fastapi import APIRouter
from fastapi import Depends , HTTPException
from backend import Crud as crud
from backend.core.confi import get_db
from sqlalchemy.orm import Session
from backend.schemas.response import UserSchema, Response, RegiSchema, ProductSchema, OrderSchema
from backend.core.token import MyHTTPBearer 
from backend.Crud import authenticate
from backend.core.token import create_token

router = APIRouter()
bearer = MyHTTPBearer()


@router.post("/login")
async def login(request: UserSchema, db: Session = Depends(get_db)):

    _authentication = authenticate(db=db, user=request)

    if _authentication is not None:
        token = create_token(_authentication.password_hash)

        return Response(
            code='Ok',
            status='200',
            message='Login Successful',
            result={'access_token': token, 'token_type': 'bearer'}
        )

    return Response(
        code='Error',
        statu='401',
        message="Incorrect credentials"
    )

@router.post('/users', dependencies=[Depends(bearer)])
async def create_user_name(request: UserSchema, db: Session = Depends(get_db)):
    try:
        user = await crud.login(db, users=request)
        return {
            "status": "ok",
            "code": "200",
            "message": "Usuario creado",
            "result": user
        }
    except HTTPException as http_err:
        raise http_err
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {err}")
    

@router.post('/create')
async def create_regi(request:RegiSchema, db:Session = Depends(get_db)):
    crud.create_user(db, RegiUser = request)
    print(request)
    return Response(status="ok",
                    code="200",
                    message="creado registro", result=request.dict(exclude_none=True))


@router.get('/producto')
async def mostrar_producto( db: Session = Depends(get_db)):
    try:
        productos = crud.mostrar_product(db)
        return productos
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostrar el producto: {e}")
    



@router.post("/inset_orden")
async def insert_orden(request: OrderSchema, db: Session = Depends(get_db)):
    try:
        crud.insert_orden(db, orderResponse  = request)
        return Response(status="ok",
                    code="200",
                    message="insertar orden", result=request.dict(exclude_none=True))
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error de insertar pedido: {e}")