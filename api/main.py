from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from api.routes.proyectos import router as proyectos_router
from api.routes.tareas import router as tareas_router
from api.routes.usuarios import router as usuarios_router
from api.template_config import STATIC_DIR, templates
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa la base de datos al arrancar la aplicacion."""
    init_db()
    yield


app = FastAPI(
    title="TaskFlow API",
    description="Sistema de gestion de proyectos y tareas",
    version="2.0.0",
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.include_router(usuarios_router)
app.include_router(proyectos_router)
app.include_router(tareas_router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
