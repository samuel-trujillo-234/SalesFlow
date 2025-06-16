import pytest
from crm.models import Cliente

@pytest.mark.django_db
def test_cliente_creation():
    cliente = Cliente.objects.create(
        nombre="Test Cliente",
        email="test@cliente.com",
        telefono="123456789",
        empresa="Test Empresa",
        notas="Notas de prueba",
    )
    assert cliente.nombre == "Test Cliente"
    assert cliente.email == "test@cliente.com"

@pytest.mark.django_db
def test_tarea_creation():
    # Similar test for Tarea model
    pass

@pytest.mark.django_db
def test_venta_creation():
    # Similar test for Venta model
    pass
