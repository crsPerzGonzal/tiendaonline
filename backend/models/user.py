from pydantic import BaseModel

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