from datetime import datetime
from .usuario import Usuario
from .tarea import Tarea
from .enums import EstadoTarea, PrioridadTarea


class Proyecto:
    """Agrupa multiples tareas y tiene un líder (Usuario)

    Atributos:
        nombre (str): Nombre del proyecto, minimo 3 caracteres
        descripcion (str, opcional): Descripción del proyecto
        lider (Usuario): Referencia al usuario líder
        tareas (list[Tarea]): Lista de tareas (Relación de composición)
        fecha_creacion (datetime): Se asigna automáticamente
    """

    def __init__(
        self, nombre: str, lider: Usuario, descripcion: str | None = None
    ) -> None:
        """Comienza un nuevo Proyecto

        Args:
            nombre: Nombre del proyecto
            lider: Usuario líder
            descripcion: Detalles (opcional)
        """
        self._validar_nombre(nombre)
        self._nombre: str = nombre
        self._descripcion: str | None = descripcion
        self._lider: Usuario = lider
        # Composición: inicia vacía
        self._tareas: list[Tarea] = []
        self._fecha_creacion: datetime = datetime.now()

    # Propiedades y Validaciones #

    @property
    def nombre(self) -> str:
        """Retorna el nombre del proyecto"""
        return self._nombre

    def _validar_nombre(self, nombre: str) -> None:
        """Valida que el nombre cumpla las reglas

        Raises:
            ValueError: Si el nombre tiene menos de 3 caracteres
        """
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")

    @property
    def descripcion(self) -> str | None:
        """Retorna la descripcion"""
        return self._descripcion

    @property
    def lider(self) -> Usuario:
        """Retorna el usuario lider"""
        return self._lider

    @property
    def fecha_creacion(self) -> datetime:
        """Retorna la fecha de creacion"""
        return self._fecha_creacion

    @property
    def tareas(self) -> list[Tarea]:
        """Retorna la lista de tareas del proyecto."""
        return self._tareas

    @property
    def esta_completado(self) -> bool:
        """Indica si todas las tareas del proyecto están completadas."""
        return bool(self._tareas) and all(
            tarea.estado == EstadoTarea.Completada for tarea in self._tareas
        )

    # Métodos Obligatorios #

    def agregar_tarea(self, tarea: Tarea) -> None:
        """Agrega una tarea al proyecto

        Args:
            tarea: La tarea a agregar
        """
        # Al ser composición, la tarea pertenece al proyecto #
        self._tareas.append(tarea)

    def obtener_tareas_pendientes(self) -> list[Tarea]:
        """Retorna las tareas que no han sido completadas

        Returns:
            list[Tarea]: Una lista filtrada de tareas
        """
        return [t for t in self._tareas if t.estado != EstadoTarea.Completada]

    def obtener_tareas_por_prioridad(
        self, prioridad: PrioridadTarea
    ) -> list[Tarea]:
        """Retorna las tareas filtradas por su prioridad

        Args:
            prioridad: Nivel de prioridad a buscar

        Returns:
            list[Tarea]: Una lista filtrada de tareas
        """
        return [t for t in self._tareas if t.prioridad == prioridad]

    def __str__(self) -> str:
        """Retorna una representación en cadena del proyecto

        Format: El nombre del proyecto
        """
        return self.nombre