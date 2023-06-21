from fastapi import FastAPI
from fastapi.responses import HTMLResponse
 
 #carpeta config
from config.database import engine, base
#carpeta routers
from routers.bread import bread_router
from routers.files import file_router
from routers.auth import auth_router
#carpeta middlewares
from middlewares.error_handler import ErrorHandler 

app = FastAPI()
app.title = "Bakery PAREDES"
app.version = "0.0.1"

base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(bread_router)
app.include_router(file_router)
app.add_middleware(ErrorHandler)

@app.get("/saludos", tags=["Welcome"])
def Welcome_API():
    return HTMLResponse(content="<h1> WELCOME TO BAKERY API </h1>")

