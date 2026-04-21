import pytest
from src.domain.usuario import Usuario
from src.domain.proyecto import Proyecto
from src.domain.tarea import Tarea
from src.domain.enums import PrioridadTarea

@pytest.fixture
def usuario_ejemplo():
    "Fixture: Usuario válido para pruebas"
    return Usuario("Emanuel21", "emanuel@correo.com", "Emanuel Cano")

@pytest.fixture
def proyecto_ejemplo(usuario_ejemplo):
    "Fixture: Proyecto con líder"
    return Proyecto(nombre="App Movil", lider=usuario_ejemplo)

@pytest.fixture
def tarea_ejemplo():
    "Fixture: Tarea pendiente por defecto"
    return Tarea(titulo="Test Unitario", prioridad=PrioridadTarea.MEDIA)

@pytest.fixture
def proyecto_con_tareas(proyecto_ejemplo, tarea_ejemplo):
    "Fixture: Proyecto poblado con una tarea"
    proyecto_ejemplo.agregar_tarea(tarea_ejemplo)
    return proyecto_ejemplo
