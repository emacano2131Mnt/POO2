from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from api.template_config import templates
from app.database import get_db
from app.models.proyecto import Proyecto
from app.models.usuario import Usuario

router = APIRouter(prefix="/proyectos", tags=["proyectos"])

# ID del usuario global por defecto (se crea al iniciar la app si no existe)
USUARIO_DEFAULT_USERNAME = "admin"


def _get_or_create_usuario_default(db: Session) -> Usuario:
    """Obtiene o crea el usuario por defecto para proyectos."""
    usuario = db.query(Usuario).filter(Usuario.username == USUARIO_DEFAULT_USERNAME).first()
    if not usuario:
        usuario = Usuario(
            username=USUARIO_DEFAULT_USERNAME,
            email="admin@taskflow.com",
            hashed_password="",
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
    return usuario


@router.get("/", response_class=HTMLResponse)
async def listar_proyectos(request: Request, db: Session = Depends(get_db)):
    """Renderiza la lista de proyectos desde la base de datos."""
    proyectos = db.query(Proyecto).all()
    return templates.TemplateResponse(
        request=request,
        name="proyectos/lista.html",
        context={"proyectos": proyectos},
    )


@router.get("/nuevo", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    """Renderiza el formulario de creacion de proyecto."""
    return templates.TemplateResponse(request=request, name="proyectos/form.html")


@router.post("/crear", response_class=HTMLResponse)
async def crear_proyecto(
    request: Request,
    nombre: str = Form(...),
    descripcion: str | None = Form(None),
    db: Session = Depends(get_db),
):
    """Crea un proyecto y lo persiste en la base de datos."""
    usuario = _get_or_create_usuario_default(db)
    nuevo_proyecto = Proyecto(
        nombre=nombre,
        descripcion=descripcion,
        usuario_id=usuario.id,
    )
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)

    proyectos = db.query(Proyecto).all()
    return templates.TemplateResponse(
        request=request,
        name="proyectos/lista.html",
        context={"proyectos": proyectos},
    )


@router.get("/{proyecto_id}")
async def obtener_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    """Retorna un proyecto por su ID."""
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return {
        "id": proyecto.id,
        "nombre": proyecto.nombre,
        "descripcion": proyecto.descripcion,
        "usuario_id": proyecto.usuario_id,
    }
