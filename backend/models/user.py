from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class User(BaseModel):
     username: str
     password_hash: str

class regiUser(BaseModel):
     username: str
     email:str
     password_hash: str
     
class product(BaseModel):
      product_id: int
      name: str
      price: float
      image_url: str
      description: str


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"

class OrderResponse(BaseModel):
    user_id: int
    order_date: datetime  # Asegúrate de que sea un datetime
    status: OrderStatus
    total_amount: float