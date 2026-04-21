from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.proyecto import Proyecto


class Usuario(Base):
    """Modelo SQLAlchemy para la entidad Usuario.

    Representa un usuario del sistema que puede liderar proyectos.

    Atributos:
        id: Clave primaria autoincremental.
        username: Nombre de usuario único (max 50 chars).
        email: Correo electrónico único (max 100 chars).
        hashed_password: Contraseña hasheada (max 255 chars).
        activo: Estado de la cuenta, por defecto True.
        fecha_registro: Fecha/hora de creación automática.
        proyectos: Relación One-to-Many con Proyecto.
    """

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    activo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    fecha_registro: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    # Relación One-to-Many: Un usuario puede tener muchos proyectos
    proyectos: Mapped[List["Proyecto"]] = relationship(
        "Proyecto", back_populates="usuario", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Usuario(id={self.id!r}, username={self.username!r}, email={self.email!r})"
