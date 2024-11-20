from sqlalchemy.orm import Session
from backend.models.user import users
from backend.schemas.response import UserSchema 

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



