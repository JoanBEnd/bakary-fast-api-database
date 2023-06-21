from fastapi import APIRouter
from schemas.auth import User
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import session
from services.auth import AuthService

from utils.encrypt import  verify_password

auth_router = APIRouter()


@auth_router.post("/login", tags=["Login"])
def login(user: User):
    db = session()
    data = AuthService(db).obtener_user(user)
          
    if verify_password(user.password, data.password) :   
    #if(user.usuario == "bakery@gmail.com" and user.password == "@auth_2023@"):
        token: str = create_token(user.dict())
        return JSONResponse(content=token)
    return JSONResponse(content={"error": "Credenciales incorrectas"})

@auth_router.post("/crear_usuario", tags=["Usuario"])
def create_user(user: User):
    db = session()
    AuthService(db).create_user(user)
    return JSONResponse(content={"message": "se registro el usuario"})

@auth_router.put("/actualizar_usuario", tags=["Usuario"])
def update_user(id: int, user: User):
    db = session()
    result = AuthService(db).obtener_user_id(id)
    if not result:        
        return JSONResponse(content={"error": "No se encontraron coincidencias"})
    AuthService(db).update_user(id, user)
    
    return JSONResponse(content={"message": "Se actualizó los datos"})

@auth_router.delete("/delete_usuario", tags=["Usuario"])
def delete_user(id: int):
    db = session()
    result = AuthService(db).obtener_user_id(id)
    if not result:        
        return JSONResponse(content={"error": "No se encontraron coincidencias"})
    AuthService(db).delete_user(id)
    
    return JSONResponse(content={"message": "Se eliminó el registro"})