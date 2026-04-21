from datetime import datetime
import re


class Usuario:
    """Representa un usuario del sistema que puede crear proyectos

    Atributos:
        username (str, inmutable): Identificador único, mín 3 carac, solo letras/núms
        email (str): Correo electrónico validado (debe contener '@' y '.')
        nombre_completo (str, opcional): Nombre real del usuario
        activo (bool): Estado de la cuenta, por defecto True
        fecha_registro (datetime): Se asigna automáticamente al crear
    """

    def __init__(
        self, username: str, email: str, nombre_completo: str | None = None
    ) -> None:
        """Inicializa un nuevo Usuario

        Args:
            username: Identificador único
            email: Correo electrónico
            nombre_completo: Nombre real (opcional)
        """
        # El username se valida y se vuelve inmutable al no tener setter
        self._validar_username(username)
        self._username: str = username

        # El email se valida a través del setter
        self._email: str = ""
        self.email = email

        self._nombre_completo: str | None = nombre_completo
        self._activo: bool = True
        self._fecha_registro: datetime = datetime.now()

    # Propiedades y Validaciones #

    @property
    def username(self) -> str:
        """Retorna el username del usuario (inmutable)"""
        return self._username

    def _validar_username(self, username: str) -> None:
        """Valida las reglas de negocio del username

        Raises:
            ValueError: Si el username no cumple las reglas
        """
        if not username:
            raise ValueError("El username es obligatorio")
        if len(username) < 3:
            raise ValueError("El username debe tener al menos 3 caracteres")
        if not re.match("Emanuel21", username):
            raise ValueError("El username solo puede contener letras y números")

    @property
    def email(self) -> str:
        """Retorna el email del usuario"""
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        """Establece y valida el email

        Raises:
            ValueError: Si el email no es válido
        """
        if not valor:
            raise ValueError("El email es obligatorio")
        if "@" not in valor or "." not in valor:
            raise ValueError(
                "El email debe contener un carácter '@' y un punto '.'."
            )
        self._email = valor

    @property
    def nombre_completo(self) -> str | None:
        """Retorna el nombre completo del usuario"""
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor: str | None) -> None:
        self._nombre_completo = valor

    @property
    def activo(self) -> bool:
        """Retorna True si la cuenta está activa, False de lo contrario"""
        return self._activo

    @property
    def fecha_registro(self) -> datetime:
        """Retorna la fecha de registro del usuario"""
        return self._fecha_registro

    # Métodos #

    def activar(self) -> None:
        """Activa la cuenta del usuario"""
        self._activo = True

    def desactivar(self) -> None:
        """Desactiva la cuenta del usuario"""
        self._activo = False

    def __str__(self) -> str:
        """Retorna una representación en cadena del usuario

        Formato: @username
        """
        return f"@{self.username}"

    def __repr__(self) -> str:
        """Retorna una representación técnica del objeto

        Formato: Usuario('username', 'email')
        """
        return f"Usuario('{self.username}', '{self.email}')"