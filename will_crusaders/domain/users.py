from typing import Union

from fastapi import Depends
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)