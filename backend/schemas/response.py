from typing import Optional, TypeVar
from pydantic import BaseModel
from datetime import datetime

T = TypeVar("T")

class UserSchema(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None

    class Config:
        from_attributes = True

class RegiSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    
    class Config:
        from_attributes = True

class ProductSchema(BaseModel):
    product_id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True

class OrderSchema(BaseModel):
    user_id: Optional[int] = None
    order_date: Optional[datetime] = None  # Cambiado a datetime
    status: Optional[str] = None
    total_amount: Optional[float] = None

    class Config:
        from_attributes = True

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]