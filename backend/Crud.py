from sqlalchemy.orm import Session
from backend.models.user import Users, Products, OrderResponse
from backend.schemas.response import UserSchema, RegiSchema, ProductSchema, OrderSchema
from fastapi import HTTPException
def get_user(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(Users).offset(Skip).limit(limit).all()


async def login(db: Session, users: UserSchema):
    _users = db.query(Users).filter(
        Users.username==users.username,
        Users.password_hash==users.password_hash
    ).first()
    if _users:
        return _users
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o contraseña incorrecta.")



def get_user_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.user_id == user_id).first()


def get_regi(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(Users).offset(Skip).limit(limit).all()



def create_user(db: Session, RegiUser: RegiSchema):
    _condicion = db.query(Users).filter (
        (Users.username == RegiUser.username) | (Users.email == RegiUser.email)

    ).first()
    if _condicion:
        raise HTTPException(status_code=400, detail="ya existe")
    _regist = Users(
        username = RegiUser.username,
        email = RegiUser.email,
        password_hash = RegiUser.password_hash

    )
    db.add(_regist)
    db.commit()
    db.refresh(_regist)
    return _regist

def get_regi_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.user_id == user_id).first()


def get_product(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(Products).offset(Skip).limit(limit).all()


def mostrar_product(db: Session):
    try:
        productos = db.query(Products).all()
        return productos 
    except Exception as e:
        raise RuntimeError(f"Error al mostrar los productos: {e}")

def get_producto_id(db: Session, product_id: int):
    return db.query(Products).filter(Products.product_id == product_id).first()


def get_orden(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(OrderResponse).offset(Skip).limit(limit).all()


def insert_orden(db: Session, orderResponse: OrderSchema):
    _order = OrderResponse(
        order_date=orderResponse.order_date,
        status=orderResponse.status,
        total_amount=orderResponse.total_amount
    )
    db.add(_order) 
    db.commit()
    return _order


def get_orfer_by_id(db: Session, user_id: int):
    return db.query(OrderResponse).filter(OrderResponse.user_id == user_id).first()