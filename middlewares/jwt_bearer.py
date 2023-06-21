from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token
from fastapi.security import HTTPBearer


class JWTBeater(HTTPBearer):
    async def __call__(self, request: Request) :
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["usuario"] != "bakery@gmail.com":
            return HTTPException(status_code=403, detail="Credenciales incorrectas")
        
