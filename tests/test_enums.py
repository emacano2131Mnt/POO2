from src.domain.enums import PrioridadTarea, EstadoTarea

def test_valores_prioridad():
    "Verifica que los valores de prioridad sean enteros."
    assert PrioridadTarea.ALTA == 1
    assert PrioridadTarea.MEDIA == 2
    assert PrioridadTarea.BAJA == 3

def test_valores_estado():
    "Verifica que los valores de estado sean strings"
    assert EstadoTarea.Pendiente == "pendiente"
    assert EstadoTarea.EN_PROGRESO == "en_progreso"
    assert EstadoTarea.Completada == "completada"