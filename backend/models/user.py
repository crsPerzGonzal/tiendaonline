from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from backend.core.confi import Base


class Users(Base):
     __tablename__ = "users"
     user_id = Column(Integer, primary_key=True)
     username = Column(String(255))  # Especificamos una longitud para VARCHAR
     password_hash = Column(String(255))  # También para el password_hash


class regiUser(Base):
     __tablename__ = "regi_users"
     user_id = Column(Integer, primary_key=True)
     username = Column(String(255))  # Especificamos la longitud
     email = Column(String(255))  # Especificamos la longitud
     password_hash = Column(String(255))  # Especificamos la longitud
     
class Products(Base):
     __tablename__ = "product"
     product_id = Column(Integer, primary_key=True)
     name = Column(String(255))  # Especificamos la longitud
     price = Column(Float)
     image_url = Column(String(255))  # Especificamos la longitud
     description = Column(String(255))  # Especificamos la longitud


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"


class OrderResponse(Base):
    __tablename__ = "orders"
    user_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)  # Asegúrate de que sea un datetime
    status = Column(OrderStatus)
    total_amount = Column(Float)