from sqlalchemy.orm import Session
from backend.models.user import users, regiUser, products, OrderResponse
from backend.schemas.response import UserSchema, RegiSchema, productSchame, orderSchema

def get_user(db:Session, Skip:int=0, limit:int=100):
    return db.query(users).offset(Skip).limit(limit).all()


def create_suers(db:Session,users:UserSchema):
    _users = users (
        username = users.username,
        password_hash = users.password_hash
    )
    db.add(_users)
    db.commit()
    db.refresh(_users)
    return _users


def get_regi(db:Session, Skip:int=0, limit:int=100):
    return db.query(regiUser).offset(Skip).limit(limit).all()


def create_regi(db:Session,regiUser: RegiSchema):
    _Regia = regiUser (
        username = regiUser.username,
        email = regiUser.email,
        password_hash = regiUser.password_hash
    )
    db.add(_Regia)
    db.commit()
    db.refresh(_Regia)
    return _Regia


def get_product(db:Session, Skip:int=0, limit:int=100):
    return db.query(products).offset(Skip).limit(limit).all()


def create_product(db:Session, product: productSchame):
    _product =product (
        name = product.name,
        price = product.price,
        imagen_url = product.imagen_url,
        descripcion = product.descripcion
    ) 
    db.add(_product)
    db.commit()
    db.refresh(_product)
    return _product


def get_producto_id(db:Session, product_id:int ):
    return db.query(products).filter(products.product_id == product_id ).first()


def get_orden(db:Session, Skip:int=0, limit:int=100):
    return db.query(OrderResponse).offset(Skip).limit(limit).all()

def create_orden(db:Session,OrderResponse : orderSchema):
    _order = OrderResponse (
        order_date = OrderResponse.order_date,
        status = OrderResponse.status,
        total_amount = OrderResponse.total_amount,
        
    ) 
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order

def get_orfer_by_id(db:Session, user_id:int ):
    return db.query(OrderResponse).filter(OrderResponse.user_id == user_id).first()