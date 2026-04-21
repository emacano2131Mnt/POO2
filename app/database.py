"""Configuración central de la base de datos con SQLAlchemy 2.0.

Provee:
    - Base: clase base declarativa para todos los modelos ORM.
    - engine: motor de conexión (SQLite en desarrollo, configurable).
    - SessionLocal: fábrica de sesiones para operaciones CRUD.
    - get_db: dependency de FastAPI para inyectar sesiones.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# URL de la base de datos: usa variable de entorno o SQLite por defecto
DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "sqlite:///./taskflow.db",
)

# Para SQLite: deshabilitar el check de mismo hilo (FastAPI usa threads)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False,  # Cambiar a True para ver SQL generado en consola
)

SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    """Clase base declarativa moderna de SQLAlchemy 2.0.

    Todos los modelos ORM del proyecto deben heredar de esta clase.
    """
    pass


def get_db():
    """Dependency de FastAPI: provee una sesión de BD por request.

    Garantiza que la sesión se cierre correctamente incluso si hay errores.

    Yields:
        Session: sesión activa de SQLAlchemy.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Crea todas las tablas definidas en los modelos si no existen.

    Solo se usa en desarrollo/testing. En producción se usan migraciones Alembic.
    """
    # Importar todos los modelos para que Base los conozca antes de crear tablas
    from app.models import Usuario, Proyecto, Tarea  # noqa: F401
    Base.metadata.create_all(bind=engine)
