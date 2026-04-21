from src.domain.enums import PrioridadTarea

def test_proyecto_filtros(proyecto_con_tareas):
    pendientes = proyecto_con_tareas.obtener_tareas_pendientes()
    assert len(pendientes) == 1
    
    altas = proyecto_con_tareas.obtener_tareas_por_prioridad(PrioridadTarea.ALTA)
    assert len(altas) == 0