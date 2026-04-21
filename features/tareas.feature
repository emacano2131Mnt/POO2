Feature: Gestión de tareas
  
  Scenario: Completar una tarea (Happy Path)
    Given una tarea "Prueba" con prioridad MEDIA
    When el usuario marca la tarea como completada
    Then la tarea debe tener una fecha de completado

  Scenario: Tarea con título muy corto (Error Path)
    When intento crear una tarea con titulo "Ab"
    Then el sistema debe lanzar un ValueError

  Scenario: Iniciar tarea pendiente (Edge Case)
    Given una tarea "Prueba" en estado pendiente
    When el usuario inicia la tarea
    Then el estado debe ser en_progreso