from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # <--- IMPORTANTE
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# --- ESTA ES LA PARTE CLAVE ---
# Le decimos a FastAPI que todo lo que esté en la carpeta "static" 
# sea accesible desde la web.
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/opciones", response_class=HTMLResponse)
async def opciones(request: Request):
    # Por ahora solo redireccionamos a una página de "Hola"
    # Luego aquí pondremos la página con las opciones de cita
    return HTMLResponse("<h1>¡Hola, Crisss! Lista para elegir tu cita.</h1>")  