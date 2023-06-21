from models.bread import Bread as BreadModel
from schemas.bread import Bread 


class BreadService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_bread(self):
        result = self.db.query(BreadModel).all()
        return result
    
    def get_bread_id(self, id: int):
        result = self.db.query(BreadModel).filter(BreadModel.id == id).first()
        return result

    def create_bread(self, bread: Bread) :
        result = BreadModel(**bread.dict())
        self.db.add(result)
        self.db.commit()

        return
    
    def update_bread(self, id: int, bread: Bread):
        result = self.db.query(BreadModel).filter(BreadModel.id == id).first()
        result.producto = bread.producto
        result.precio = bread.precio
        result.descripcion = bread.descripcion
        result.tipo = bread.tipo
        
        self.db.commit()
        return
    
    def delete_bread(self, id: int):
        result = self.db.query(BreadModel).filter(BreadModel.id == id).first()
        self.db.delete(result)
        self.db.commit()
        return
        