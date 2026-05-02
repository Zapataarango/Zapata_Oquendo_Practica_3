from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud.usuario import get_user_by_email
from app.security.auth import verify_password, create_access_token
from app.security.scopes import get_scopes_for_role
from app.schemas.auth import LoginRequest, Token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/token", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, login_data.correo)
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.activo:
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    user_scopes = get_scopes_for_role(user.rol)

    token_data = {
        "sub": user.correo,
        "id_usuario": user.id_usuario,
        "rol": user.rol,
        "scopes": user_scopes
    }

    access_token = create_access_token(data=token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "rol": user.rol
    }