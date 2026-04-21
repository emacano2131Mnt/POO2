"""Configuración del entorno para Behave."""

def before_scenario(context, scenario):
    """Limpia el contexto antes de cada escenario de prueba."""
    context.usuario = None
    context.proyecto = None
    context.tarea = None
    context.error = None