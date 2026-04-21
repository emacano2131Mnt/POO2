from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import DateTime, Enum as SAEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from src.domain.enums import EstadoTarea, PrioridadTarea

if TYPE_CHECKING:
    from app.models.proyecto import Proyecto


class Tarea(Base):
    """Modelo SQLAlchemy para la entidad Tarea.

    Representa una tarea individual dentro de un Proyecto.

    Atributos:
        id: Clave primaria autoincremental.
        titulo: Título de la tarea (max 100 chars).
        descripcion: Descripción opcional.
        estado: Enum con valores pendiente, en_progreso, completada.
        prioridad: Enum con valores ALTA(1), MEDIA(2), BAJA(3).
        proyecto_id: FK hacia la tabla proyectos (nullable=False).
        fecha_creacion: Fecha/hora de creación automática.
        fecha_completado: Fecha/hora de finalización (nullable).
        proyecto: Relación Many-to-One con Proyecto.
    """

    __tablename__ = "tareas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    estado: Mapped[EstadoTarea] = mapped_column(
        SAEnum(
            EstadoTarea,
            name="estadotarea_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=EstadoTarea.Pendiente,
    )
    prioridad: Mapped[PrioridadTarea] = mapped_column(
        SAEnum(
            PrioridadTarea,
            name="prioridadtarea_enum",
            values_callable=lambda x: [str(e.value) for e in x],
        ),
        nullable=False,
        default=PrioridadTarea.MEDIA,
    )
    proyecto_id: Mapped[int] = mapped_column(
        ForeignKey("proyectos.id", ondelete="CASCADE"), nullable=False
    )
    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    fecha_completado: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, default=None
    )

    # Relación Many-to-One: Muchas tareas pertenecen a un proyecto
    proyecto: Mapped["Proyecto"] = relationship("Proyecto", back_populates="tareas")

    def __repr__(self) -> str:
        return (
            f"Tarea(id={self.id!r}, titulo={self.titulo!r}, "
            f"estado={self.estado!r}, proyecto_id={self.proyecto_id!r})"
        )
