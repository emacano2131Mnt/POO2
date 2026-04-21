from enum import Enum, unique


@unique
class PrioridadTarea(int, Enum):
    """Representa los niveles de prioridad de una tarea

    Valores:
        Alta(1): Prioridad más alta
        Media(2): Prioridad media
        Baja(3): Prioridad más baja
    """
    ALTA = 1
    MEDIA = 2
    BAJA = 3

@unique
class EstadoTarea(str, Enum):
    """Representa los posibles estados de una tarea.

    Valores:
        Pendiente: La tarea aún no empieza.
        Realizandose: La tarea está siendo realizada.
        Completada: La tarea ha finalizado.
    """

    Pendiente = "pendiente"
    EN_PROGRESO = "en_progreso"
    Completada = "completada"