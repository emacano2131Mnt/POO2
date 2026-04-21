from datetime import datetime
from .enums import PrioridadTarea, EstadoTarea


class Tarea:
    """Representa una tarea individual dentro de un proyecto

    Atributos:
        titulo (str): Titulo de la tarea, minimo 3 caracteres
        descripcion (str, opcional): Detalles de la tarea
        prioridad (PrioridadTarea): Enum con valores ALTA, MEDIA, BAJA
        estado (EstadoTarea): Enum con valores pendiente, Realizandose, completada
        fecha_creacion (datetime): Se asigna automaticamente
        fecha_completado (datetime, opcional): Se asigna al completar
    """

    def __init__(
        self,
        titulo: str,
        prioridad: PrioridadTarea,
        descripcion: str | None = None,
    ) -> None:
        """Empieza una nueva Tarea

        Args:
            titulo: Título de la tarea
            prioridad: Prioridad inicial
            descripcion: Detalles (opcional)
        """
        self._validar_titulo(titulo)
        self._titulo: str = titulo
        self._descripcion: str | None = descripcion
        self._prioridad: PrioridadTarea = prioridad
        self._estado: EstadoTarea = EstadoTarea.Pendiente
        self._fecha_creacion: datetime = datetime.now()
        self._fecha_completado: datetime | None = None

    # Propiedades y Validaciones #

    @property
    def titulo(self) -> str:
        """Retorna el titulo de la tarea"""
        return self._titulo

    def _validar_titulo(self, titulo: str) -> None:
        """Valida que el titulo cumpla las reglas

        Raises:
            ValueError: Si el titulo tiene menos de 3 caracteres
        """
        if not titulo:
            raise ValueError("El titulo es obligatorio")
        if len(titulo) < 3:
            raise ValueError("El titulo debe tener al menos 3 caracteres")

    @property
    def descripcion(self) -> str | None:
        """Retorna la descripción de la tarea"""
        return self._descripcion

    @property
    def prioridad(self) -> PrioridadTarea:
        """Retorna la prioridad de la tarea"""
        return self._prioridad

    @property
    def estado(self) -> EstadoTarea:
        """Retorna el estado de la tarea"""
        return self._estado

    @property
    def fecha_creacion(self) -> datetime:
        """Retorna la fecha de creacion"""
        return self._fecha_creacion

    @property
    def fecha_completado(self) -> datetime | None:
        """Retorna la fecha de finalizacion, si aplica"""
        return self._fecha_completado

    # Métodos #

    def completar(self) -> None:
        """Marca la tarea como completada y registra la fecha"""
        self._estado = EstadoTarea.Completada
        self._fecha_completado = datetime.now()

    def cambiar_prioridad(self, nueva_prioridad: PrioridadTarea) -> None:
        """Cambia la prioridad de la tarea

        Args:
            nueva_prioridad: El nuevo nivel de prioridad
        """
        self._prioridad = nueva_prioridad

    def iniciar(self) -> None:
        """Cambia el estado de la tarea a En_Progreso"""
        self._estado = EstadoTarea.EN_PROGRESO

    def __str__(self) -> str:
        """Retorna una representación en cadena de la tarea

        Format: [PRIORIDAD] titulo (estado)
        """
        # conseguimos el nombre del enum (ej: "ALTA")
        prioridad_nombre = self.prioridad.name
        # conseguimos el valor del enum (ej: "pendiente")
        estado_valor = self.estado.value
        return f"[{prioridad_nombre}] {self.titulo} ({estado_valor})"