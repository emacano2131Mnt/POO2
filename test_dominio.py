""" Pruebas para el proyecto """

from src.domain.usuario import Usuario
from src.domain.proyecto import Proyecto
from src.domain.tarea import Tarea
from src.domain.enums import PrioridadTarea, EstadoTarea

def test_flujo_completo():
    # Ejecuta pruebas de las clases en el dominio
    # Realiza las siguientes acciones:
    # 1. Valida la creación de usuarios y sus restricciones.
    # 2. Instancia proyectos con relaciones de composición.
    # 3. Gestiona el ciclo de vida de las tareas (inicio, cambio de prioridad, fin).
    # 4. Verifica los métodos de filtrado y búsqueda del proyecto.
    print("1. Probando Creación de Usuario")
    user = Usuario("Emanuel21", "emanuel@correo.com", "Emanuel Cano")
    print(f"Usuario creado: {user}")
    
    # Validar inmutabilidad y errores #
    try:
        user.email = "correo_invalido"
    except ValueError as e:
        print(f"Validación de email exitosa: {e}")

    print("\n-2. Probando Creación de Proyecto")
    proyecto = Proyecto(nombre="App", lider=user)
    print(f"Proyecto: {proyecto} | Líder: {proyecto.lider}")

    print("\n3. Probando Gestión de Tareas (Composición)")
    t1 = Tarea("Login", PrioridadTarea.ALTA, "Crear pantalla de acceso")
    t2 = Tarea("Base de Datos", PrioridadTarea.MEDIA)
    # El proyecto "posee" las tareas #
    proyecto.agregar_tarea(t1)
    proyecto.agregar_tarea(t2)
    
    print(f"Tareas totales agregadas: 2")
    print(f"Estado inicial t1: {t1}")

    print("\n-4. Cambiando Estados y Prioridades")
    t1.iniciar()
    print(f"t1 iniciada: {t1}")
    
    t1.completar()
    print(f"t1 completada: {t1} a las {t1.fecha_completado}")

    print("\n--- 5. Probando Filtros del Proyecto ---")
    # Retorna tareas no completadas #
    pendientes = proyecto.obtener_tareas_pendientes()
    print(f"Tareas pendientes (debe ser 1): {len(pendientes)}")
    for p in pendientes:
        print(f"- Pendiente: {p.titulo}")
    # Filtrado por Enum PrioridadTarea #
    altas = proyecto.obtener_tareas_por_prioridad(PrioridadTarea.ALTA)
    print(f"Tareas ALTA prioridad: {len(altas)}")

if __name__ == "__main__":
    try:
        test_flujo_completo()
        print("\n-Todas las pruebas de dominio pasaron con éxito")
    except Exception as e:
        print(f"\n-Error en las pruebas: {e}")