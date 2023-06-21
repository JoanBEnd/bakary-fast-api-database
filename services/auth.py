from models.user import User as UserModel
from schemas.auth import User
from utils.encrypt import hash_password

class AuthService():
    def __init__(self, db) -> None:
        self.db = db
    
    def obtener_user(self, user: User):
        
        data = self.db.query(UserModel).filter(UserModel.usuario == user.usuario).first() 
        return data

    def obtener_user_id(self, id: int):
        
        data = self.db.query(UserModel).filter(UserModel.id == id).first() 
        return data

    def create_user(self, user: User):
        password_encrip = hash_password(user.password)        
        user.password=password_encrip
        result = UserModel(**user.dict())
        self.db.add(result)
        self.db.commit()
        return
    
    def update_user(self, id: int, user: User):
        data = self.db.query(UserModel).filter(UserModel.id == id).first()
        password_encrip = hash_password(user.password)                        
        data.usuario = user.usuario
        data.password = password_encrip
        self.db.commit()
        return

    def delete_user(self, id: int):
        data = self.db.query(UserModel).filter(UserModel.id == id).first()
        self.db.delete(data)
        self.db.commit()
        return
        