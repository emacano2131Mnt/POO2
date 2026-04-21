"""agregar columna prioridad a tareas (patch para BD existentes)

Revision ID: 0002_agregar_prioridad_tarea
Revises: 0001_modelos_iniciales
Create Date: 2026-04-21 01:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0002_agregar_prioridad_tarea"
down_revision: Union[str, None] = "0001_modelos_iniciales"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Agrega columna prioridad a la tabla tareas si no existe."""
    with op.batch_alter_table("tareas") as batch_op:
        batch_op.add_column(
            sa.Column(
                "prioridad",
                sa.Enum("1", "2", "3", name="prioridadtarea_enum"),
                nullable=False,
                server_default="2",  # MEDIA por defecto
            )
        )


def downgrade() -> None:
    """Elimina la columna prioridad de tareas."""
    with op.batch_alter_table("tareas") as batch_op:
        batch_op.drop_column("prioridad")
