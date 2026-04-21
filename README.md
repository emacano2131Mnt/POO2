# TaskFlow — Sistema de Gestión de Proyectos y Tareas

## Tecnologías
- **Backend:** FastAPI + Jinja2 + HTMX + Bootstrap
- **ORM:** SQLAlchemy 2.0 (estilo declarativo moderno)
- **Migraciones:** Alembic
- **BD desarrollo:** SQLite (`taskflow.db`)
- **BD producción:** PostgreSQL / MySQL (configurable via `DATABASE_URL`)
- **Testing:** pytest, behave (BDD), pytest-cov

## Instalación y Ejecución

### 1. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Ejecutar migraciones con Alembic
```bash
# Verificar historial de migraciones
alembic history --verbose

# Ver migración actual aplicada
alembic current

# Aplicar todas las migraciones pendientes
alembic upgrade head
```

### 3. Iniciar el servidor
```bash
uvicorn api.main:app --reload
```
Abrir: http://localhost:8000

---

## Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `DATABASE_URL` | URL de conexión a la BD | `sqlite:///./taskflow.db` |

### Ejemplos de DATABASE_URL
```bash
# SQLite (desarrollo, por defecto)
DATABASE_URL=sqlite:///./taskflow.db

# PostgreSQL (producción)
DATABASE_URL=postgresql://usuario:password@localhost:5432/taskflow

# MySQL (producción)
DATABASE_URL=mysql+mysqlclient://usuario:password@localhost:3306/taskflow
```

---

## Modelos de Base de Datos

### Relaciones
```
Usuario (1) ──────── (N) Proyecto
Proyecto (1) ─────── (N) Tarea
```

### Usuario
| Campo | Tipo | Constraint |
|-------|------|------------|
| id | Integer | PK, autoincrement |
| username | String(50) | UNIQUE, NOT NULL |
| email | String(100) | UNIQUE, NOT NULL |
| hashed_password | String(255) | NOT NULL |
| activo | Boolean | NOT NULL, default=True |
| fecha_registro | DateTime | NOT NULL |

### Proyecto
| Campo | Tipo | Constraint |
|-------|------|------------|
| id | Integer | PK, autoincrement |
| nombre | String(100) | NOT NULL |
| descripcion | Text | nullable |
| usuario_id | Integer | FK → usuarios.id |
| fecha_creacion | DateTime | NOT NULL |

### Tarea
| Campo | Tipo | Constraint |
|-------|------|------------|
| id | Integer | PK, autoincrement |
| titulo | String(100) | NOT NULL |
| descripcion | Text | nullable |
| estado | Enum | pendiente/en_progreso/completada |
| proyecto_id | Integer | FK → proyectos.id |
| fecha_creacion | DateTime | NOT NULL |
| fecha_completado | DateTime | nullable |

---

## Tests

```bash
# Tests unitarios
pytest tests/ -v --cov=src --cov=app

# Tests BDD
behave features/
```
