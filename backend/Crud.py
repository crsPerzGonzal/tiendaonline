from sqlalchemy.orm import Session
from backend.models.user import Users, regiUser, Products, OrderResponse
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
    return db.query(regiUser).offset(Skip).limit(limit).all()



def create_user(db: Session, RegiUser: RegiSchema):
    # Verifica si el usuario ya existe
    existing_user = db.query(RegiUser).filter(RegiUser.email == regiUser.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")
    
    # Crea una nueva instancia del usuario
    new_user = RegiUser(
        username=regiUser.username,
        email=regiUser.email,
        password_hash=regiUser.password_hash
    )
    try:
        # Agregar a la sesión y guardar en la base de datos
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Actualizar la instancia
        return new_user
    except Exception as e:
        db.rollback()  # Revertir cambios si hay un error
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")

def get_regi_id(db: Session, user_id: int):
    return db.query(regiUser).filter(regiUser.user_id == user_id).first()


def get_product(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(Products).offset(Skip).limit(limit).all()


def create_product(db: Session, product: ProductSchema):
    # Corrección: usar el constructor de la clase Products, no el de ProductSchema
    _product = Products(
        name=product.name,
        price=product.price,
        image_url=product.image_url,
        description=product.description  # Corrección: cambió 'descriptions' a 'description'
    )
    db.add(_product)
    db.commit()
    db.refresh(_product)
    return _product


def get_producto_id(db: Session, product_id: int):
    return db.query(Products).filter(Products.product_id == product_id).first()


def get_orden(db: Session, Skip: int = 0, limit: int = 100):
    return db.query(OrderResponse).offset(Skip).limit(limit).all()


def create_orden(db: Session, orderResponse: OrderSchema):
    # Corrección: usar el constructor de la clase OrderResponse, no el de OrderSchema
    _order = OrderResponse(
        order_date=orderResponse.order_date,
        status=orderResponse.status,
        total_amount=orderResponse.total_amount
    )
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order


def get_orfer_by_id(db: Session, user_id: int):
    return db.query(OrderResponse).filter(OrderResponse.user_id == user_id).first()