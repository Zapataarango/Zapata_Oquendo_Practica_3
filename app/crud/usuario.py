from sqlalchemy.orm import Session
from app.models import Usuario
from app.schemas.usuario import UsuarioCreate
from app.security.auth import hash_password

def obtener_usuario_por_correo(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.correo == email).first()

def obtener_usuario_por_id(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == user_id).first()

def listar_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_pwd = hash_password(usuario.password)
    db_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        rol=usuario.rol,
        password_hash=hashed_pwd,
        activo=True
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario