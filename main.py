from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory=".")

# Lista de usuarios válidos
valid_users = ["Jairo", "Christian", "Pepito", "Ana"]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, username: str = None):
    if username in valid_users:
        mensaje = f"Hola {username}, bienvenido/a"
        return templates.TemplateResponse("index.html", {"request": request, "username": username, "message": mensaje, "X": [1, 2, 3, 4, 5]})
    else:
        mensaje = "No ha ingresado un usuario válido"
        return templates.TemplateResponse("index_basico.html", {"request": request, "username": username, "message": mensaje})

@app.get('/endpoint1', response_class=HTMLResponse)
async def endpoint1(request: Request, username: str = None):
    if username:
        mensaje = f'Hola {username}, aquí tienes tu lista de tareas'
        X = [f"Tarea {i+1}" for i in range(5)]
        return templates.TemplateResponse("endpoint1.html", {"request": request, "username": username, "message": mensaje, "X": X})
    else:
        mensaje = 'No se proporcionó ningún usuario'
        return templates.TemplateResponse("endpoint1.html", {"request": request, "username": "", "message": mensaje, "X": []})

@app.get('/ruta/endpoint1', response_class=HTMLResponse)
async def endpoint3(request: Request, username: str = None):
    if username:
        mensaje = f'Hola {username}, este es el endpoint 1 en la ruta'
        return templates.TemplateResponse("endpoint1_2.html", {"request": request, "username": username, "message": mensaje})
    else:
        mensaje = 'No se proporcionó ningún usuario'
        return templates.TemplateResponse("endpoint1_2.html", {"request": request, "username": "", "message": mensaje})
