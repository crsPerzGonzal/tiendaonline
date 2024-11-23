from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from backend.core.confi import Base


class Users(Base):
     __tablename__ = "users"
     user_id = Column(Integer, primary_key=True)
     username = Column(String(255))  
     password_hash = Column(String(255))
     email = Column(String(255))

     
class Products(Base):
     __tablename__ = "products"
     product_id = Column(Integer, primary_key=True)
     name = Column(String(255)) 
     price = Column(Float)
     image_url = Column(String(255))  
     description = Column(String(255))  

class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class OrderResponse(Base):
    __tablename__ = "orders"
    user_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    status = Column(OrderStatus)
    total_amount = Column(Float)