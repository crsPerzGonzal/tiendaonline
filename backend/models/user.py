from sqlalchemy import column, Integer, String, Float, DATETIME, Enum
from backend.core.confi import Base


class users(Base):
     #table name
     __tablename__ = "users"

     username = column(String)
     password_hash = column(String)

class regiUser(Base):

     __tablename__ = "users"

     username = column(String)
     email = column(String)
     password_hash = column(String)
     
class products(Base):
      
      __tablename__ = "products"

      product_id = column(Integer, primary_key=True)
      name = column(String)
      price = column(Float)
      image_url = column(String)
      description = column(String)


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"

class OrderResponse(Base):
    
    __tablename__ = "orders"

    user_id = column(Integer, primary_key = True)
    order_date = column(DATETIME)  # Asegúrate de que sea un datetime
    status = column(OrderStatus)
    total_amount = column(Float)