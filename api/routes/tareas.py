from datetime import datetime

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from api.template_config import templates
from app.database import get_db
from app.models.proyecto import Proyecto
from app.models.tarea import Tarea
from src.domain.enums import EstadoTarea, PrioridadTarea

router = APIRouter(prefix="/tareas", tags=["tareas"])


@router.get("/{proyecto_id}", response_class=HTMLResponse)
async def obtener_lista_tareas(
    proyecto_id: int, request: Request, db: Session = Depends(get_db)
):
    """Retorna las tareas de un proyecto desde la base de datos."""
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return templates.TemplateResponse(
        request=request,
        name="tareas/lista.html",
        context={"tareas": proyecto.tareas, "proyecto_id": proyecto_id},
    )


@router.post("/{proyecto_id}/agregar", response_class=HTMLResponse)
async def agregar_tarea(
    proyecto_id: int,
    request: Request,
    titulo: str = Form(...),
    prioridad: int = Form(...),
    db: Session = Depends(get_db),
):
    """Agrega una nueva tarea al proyecto y la persiste."""
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    nueva_tarea = Tarea(
        titulo=titulo,
        estado=EstadoTarea.Pendiente,
        prioridad=PrioridadTarea(prioridad),
        proyecto_id=proyecto_id,
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(proyecto)

    return templates.TemplateResponse(
        request=request,
        name="tareas/lista.html",
        context={"tareas": proyecto.tareas, "proyecto_id": proyecto_id},
    )


@router.patch("/{proyecto_id}/{tarea_id}/completar", response_class=HTMLResponse)
async def completar_tarea(
    proyecto_id: int,
    tarea_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    """Marca una tarea como completada y persiste el cambio."""
    proyecto = db.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    tarea = db.get(Tarea, tarea_id)
    if not tarea or tarea.proyecto_id != proyecto_id:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea.estado = EstadoTarea.Completada
    tarea.fecha_completado = datetime.utcnow()
    db.commit()
    db.refresh(tarea)

    return templates.TemplateResponse(
        request=request,
        name="tareas/item.html",
        context={"tarea": tarea, "p_id": proyecto_id, "t_id": tarea_id},
    )
