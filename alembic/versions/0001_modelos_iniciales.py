"""modelos_iniciales: crea tablas usuarios, proyectos y tareas

Revision ID: 0001_modelos_iniciales
Revises:
Create Date: 2026-04-21 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0001_modelos_iniciales"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Crea las tres tablas principales del sistema TaskFlow."""

    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False),
        sa.Column("fecha_registro", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )

    op.create_table(
        "proyectos",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nombre", sa.String(length=100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("usuario_id", sa.Integer(), nullable=False),
        sa.Column("fecha_creacion", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["usuario_id"], ["usuarios.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "tareas",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("titulo", sa.String(length=100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column(
            "estado",
            sa.Enum("pendiente", "en_progreso", "completada", name="estadotarea_enum"),
            nullable=False,
        ),
        sa.Column(
            "prioridad",
            sa.Enum("1", "2", "3", name="prioridadtarea_enum"),
            nullable=False,
        ),
        sa.Column("proyecto_id", sa.Integer(), nullable=False),
        sa.Column("fecha_creacion", sa.DateTime(), nullable=False),
        sa.Column("fecha_completado", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["proyecto_id"], ["proyectos.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Elimina las tres tablas en orden inverso (respetando FK)."""
    op.drop_table("tareas")
    op.drop_table("proyectos")
    op.drop_table("usuarios")
