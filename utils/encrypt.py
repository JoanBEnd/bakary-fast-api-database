from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(input_pass: str, hashed_pass: str):
    return pwd_context.verify(input_pass, hashed_pass)