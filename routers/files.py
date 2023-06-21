from fastapi import APIRouter, File, UploadFile,Depends
from middlewares.jwt_bearer import JWTBeater
file_router = APIRouter()
@file_router.post("/upload-file/", tags=["Files"], dependencies=[Depends(JWTBeater())])
async def upload_file(my_file: UploadFile = File(...)):
    file_path = f"documents/{my_file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await my_file.read())
    return {"filename": my_file.filename}