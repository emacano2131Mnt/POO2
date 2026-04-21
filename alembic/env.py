"""Configuración del entorno de Alembic.

Importa Base.metadata desde app.database para que Alembic detecte
automáticamente todos los modelos ORM al generar migraciones.
"""

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# Agregar el directorio raíz del proyecto al path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar Base para que Alembic conozca todos los modelos
from app.database import Base  # noqa: E402
# Importar modelos explícitamente para registrarlos en metadata
from app.models import Usuario, Proyecto, Tarea  # noqa: F401, E402

# Configuración de Alembic desde alembic.ini
config = context.config

# Interpretar el fichero de logging si existe
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadata apunta al metadata de todos los modelos ORM
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo 'offline' (sin conexión activa).

    Útil para generar SQL sin conectar a la BD.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,  # Necesario para SQLite (ALTER TABLE limitado)
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta migraciones en modo 'online' (con conexión activa).

    Crea el engine a partir de la URL en alembic.ini.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # Necesario para SQLite
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
