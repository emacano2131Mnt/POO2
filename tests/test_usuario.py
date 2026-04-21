import pytest
from src.domain.usuario import Usuario

def test_usuario_activar_desactivar(usuario_ejemplo):
    usuario_ejemplo.desactivar()
    assert usuario_ejemplo.activo is False
    usuario_ejemplo.activar()
    assert usuario_ejemplo.activo is True

@pytest.mark.parametrize("u, e", [("ab", "a@b.c"), ("user!", "a@b.c"), ("user", "mail")])
def test_usuario_excepciones(u, e):
    with pytest.raises(ValueError):
        Usuario(u, e)