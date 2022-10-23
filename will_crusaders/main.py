# from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from config import LOGIN_SECRET

DB = {
    'users': {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
}

app = FastAPI()
manager = LoginManager(LOGIN_SECRET, token_url='/auth/token', use_cookie=True)


@app.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token}


@app.get("/")
# def read_root(token: str = Depends(oauth2_scheme)):
#    return {"token": token}
@manager.user_loader()
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)
