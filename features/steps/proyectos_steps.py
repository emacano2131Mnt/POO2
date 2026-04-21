from behave import given, when, then
from src.domain.usuario import Usuario
from src.domain.proyecto import Proyecto
from src.domain.tarea import Tarea
from src.domain.enums import PrioridadTarea

@given('un líder de proyecto con username "{username}"')
def step_impl(context, username):
    context.usuario = Usuario(username, "lider@test.com")

@when('el líder crea un proyecto llamado "{nombre_proyecto}"')
def step_impl(context, nombre_proyecto):
    context.proyecto = Proyecto(nombre=nombre_proyecto, lider=context.usuario)

@when('agrega una tarea "{titulo_tarea}" de prioridad ALTA')
def step_impl(context, titulo_tarea):
    tarea = Tarea(titulo=titulo_tarea, prioridad=PrioridadTarea.ALTA)
    context.proyecto.agregar_tarea(tarea)

@then('el proyecto debe tener {cantidad:d} tarea en su lista')
def step_impl(context, cantidad):
    # Validamos que la composición funcione #
    pendientes = context.proyecto.obtener_tareas_pendientes()
    assert len(pendientes) == cantidad