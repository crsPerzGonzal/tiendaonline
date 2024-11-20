from typing import list, Optional, Generic, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel


T = TypeVar("T")

class UserSchema(BaseModel):
    username = Optional[str] = None
    password_hash = Optional[str] = None

    class Config:
        orm_mode = True

class RegiSchema(BaseModel):
    username = Optional[str] = None
    email = Optional[str] = None
    password_hash = Optional[str] = None
    
    class Config:
        orm_mode = True


class productSchame(BaseModel):
    product_id = Optional[int] = None
    name = Optional[str] = None
    price = Optional[float] = None
    imagen_url = Optional[str] = None
    descripcion = Optional[str] = None

    class Config:
        orm_mode = True

class orderSchema(BaseModel):
    user_id = Optional[int] = None
    order_date = Optional[str] = None
    Status = Optional[str] = None
    total_amount = Optional[float] = None

    class Config:
        orm_mode = True

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]





