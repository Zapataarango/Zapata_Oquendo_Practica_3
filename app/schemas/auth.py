from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    correo: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    rol: str