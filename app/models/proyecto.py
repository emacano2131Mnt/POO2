from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.tarea import Tarea


class Proyecto(Base):
    """Modelo SQLAlchemy para la entidad Proyecto.

    Agrupa múltiples tareas y pertenece a un Usuario líder.

    Atributos:
        id: Clave primaria autoincremental.
        nombre: Nombre del proyecto (max 100 chars).
        descripcion: Descripción opcional.
        usuario_id: FK hacia la tabla usuarios (nullable=False).
        fecha_creacion: Fecha/hora de creación automática.
        usuario: Relación Many-to-One con Usuario.
        tareas: Relación One-to-Many con Tarea.
    """

    __tablename__ = "proyectos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False
    )
    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    # Relación Many-to-One: Muchos proyectos pertenecen a un usuario
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="proyectos")

    # Relación One-to-Many: Un proyecto tiene muchas tareas
    tareas: Mapped[List["Tarea"]] = relationship(
        "Tarea", back_populates="proyecto", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"Proyecto(id={self.id!r}, nombre={self.nombre!r}, "
            f"usuario_id={self.usuario_id!r})"
        )
