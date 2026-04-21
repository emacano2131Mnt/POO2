Feature: Gestión de usuarios
  Como administrador del sistema
  Quiero gestionar las cuentas de usuario
  Para controlar el acceso al sistema

  Background:
    Given un usuario registrado con username "Emanuel21"

  Scenario: Activar y desactivar cuenta (Escenario feliz)
    When el administrador desactiva la cuenta
    Then el estado del usuario debe ser inactivo
    And si el administrador activa la cuenta
    Then el estado del usuario debe ser activo