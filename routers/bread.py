from fastapi import APIRouter, Depends
from schemas.bread import Bread
from config.database import session
from services.bread import BreadService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBeater
bread_router = APIRouter()


@bread_router.get("/get_bread", tags=["Bakery"], dependencies=[Depends(JWTBeater())])
def get_breads():
    db = session()
    result = BreadService(db).get_bread()
    return JSONResponse(content=jsonable_encoder(result))

@bread_router.get("/get_bread/{id}", tags=["Bakery"], dependencies=[Depends(JWTBeater())])
def get_bread(id: int):
    db = session()
    result = BreadService(db).get_bread_id(id)
    return JSONResponse(content=jsonable_encoder(result))

@bread_router.post("/create_bread", tags=["Bakery"], dependencies=[Depends(JWTBeater())])
def crear_bread(bread: Bread):
    db = session()     
    BreadService(db).create_bread(bread)
    return JSONResponse(content={"message": "se registro el pan"})

@bread_router.put("/update_bread", tags=["Bakery"], dependencies=[Depends(JWTBeater())])
def update_bread(id: int, bread: Bread):
    db = session()
    result = BreadService(db).get_bread_id(id)
    if not result:
        return JSONResponse(content={"error": "No se encontraron coincidencias"})
    
    BreadService(db).update_bread(id, bread)
    return



@bread_router.delete("/delete_bread", tags=["Bakery"], dependencies=[Depends(JWTBeater())])
def delete_bread(id: int):
    db = session()
    result = BreadService(db).get_bread_id(id)
    if not result:
        return JSONResponse(content={"error": "No se encontraron coincidencias"})
    
    BreadService(db).delete_bread(id)    
    return JSONResponse(content={"message": "Se actualizó los datos"})
