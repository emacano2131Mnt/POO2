from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from api.template_config import templates
from app.database import get_db
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("/", response_class=HTMLResponse)
async def listar_usuarios(request: Request, db: Session = Depends(get_db)):
    """Retorna la lista de usuarios desde la base de datos."""
    usuarios = db.query(Usuario).all()
    return templates.TemplateResponse(
        request=request,
        name="usuarios/lista.html",
        context={"usuarios": usuarios},
    )


@router.post("/", status_code=201)
async def crear_usuario(
    username: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    """Crea un nuevo usuario y lo persiste en la base de datos."""
    if len(username) < 3:
        raise HTTPException(status_code=422, detail="El username debe tener al menos 3 caracteres")
    if "@" not in email or "." not in email:
        raise HTTPException(status_code=422, detail="El email no es valido")

    nuevo_usuario = Usuario(username=username, email=email, hashed_password="")
    db.add(nuevo_usuario)
    try:
        db.commit()
        db.refresh(nuevo_usuario)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username o email ya existe")

    return {"message": "Usuario creado con exito", "username": username, "id": nuevo_usuario.id}


@router.get("/{usuario_id}")
async def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Busca un usuario por su ID en la base de datos."""
    usuario = db.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {
        "id": usuario.id,
        "username": usuario.username,
        "email": usuario.email,
        "activo": usuario.activo,
    }
