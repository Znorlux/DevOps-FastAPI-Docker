from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
ruta = APIRouter()

templates = Jinja2Templates(directory="ruta2")

@ruta.get('/endpoint2', response_class=HTMLResponse)
def endpoint2(request: Request, username: str = None):
    mensaje = 'Este es el endpoint 2'
    return templates.TemplateResponse("endpoint2.html", {"request": request, "username": username, "message": mensaje})