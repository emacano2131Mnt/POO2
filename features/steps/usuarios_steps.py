from behave import given, when, then
from src.domain.usuario import Usuario

@given('un usuario con username "{username}" y email "{email}"')
def step_impl(context, username, email):
    context.usuario = Usuario(username=username, email=email)

@when('el administrador desactiva su cuenta')
def step_impl(context):
    context.usuario.desactivar()

@then('la cuenta debe figurar como inactiva')
def step_impl(context):
    assert context.usuario.activo is False

@when('intento registrar un usuario con email "{email_invalido}"')
def step_impl(context, email_invalido):
    try:
        Usuario(username="user123", email=email_invalido)
        context.error = None
    except ValueError as e:
        context.error = e