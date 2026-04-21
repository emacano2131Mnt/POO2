def test_tarea_completar(tarea_ejemplo):
    tarea_ejemplo.completar()
    assert tarea_ejemplo.fecha_completado is not None