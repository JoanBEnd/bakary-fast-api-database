from jwt import decode, encode

def create_token(data: dict):

    token: str = encode(payload=data,key="my_secret_key", algorithm="HS256" )
    return token

def validate_token(token: str):

    data: str =decode(token, key="my_secret_key", algorithms=["HS256"])
    return data