from behave import given, when, then
from src.domain.tarea import Tarea
from src.domain.enums import PrioridadTarea, EstadoTarea
import pytest

@given('una tarea "{titulo}" con prioridad MEDIA')
def step_impl(context, titulo):
    context.tarea = Tarea(titulo=titulo, prioridad=PrioridadTarea.MEDIA)

@when('el usuario marca la tarea como completada')
def step_impl(context):
    context.tarea.completar()

@then('la tarea debe tener una fecha de completado')
def step_impl(context):
    assert context.tarea.fecha_completado is not None
    assert context.tarea.estado == EstadoTarea.Completada

@when('intento crear una tarea con titulo "{titulo}"')
def step_impl(context, titulo):
    try:
        Tarea(titulo=titulo, prioridad=PrioridadTarea.BAJA)
        context.error = None
    except ValueError as e:
        context.error = e

@then('el sistema debe lanzar un ValueError')
def step_impl(context):
    assert isinstance(context.error, ValueError)

@given('una tarea "{titulo}" en estado pendiente')
def step_impl(context, titulo):
    context.tarea = Tarea(titulo=titulo, prioridad=PrioridadTarea.BAJA)
    assert context.tarea.estado == EstadoTarea.Pendiente

@when('el usuario inicia la tarea')
def step_impl(context):
    context.tarea.iniciar()

@then('el estado debe ser en_progreso')
def step_impl(context):
    assert context.tarea.estado == EstadoTarea.EN_PROGRESO