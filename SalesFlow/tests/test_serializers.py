import pytest
from crm.serializers import ClienteSerializer

@pytest.mark.django_db
def test_cliente_serializer():
    data = {
        "nombre": "Test Cliente",
        "email": "test@cliente.com",
        "telefono": "123456789",
        "empresa": "Test Empresa",
        "notas": "Notas de prueba",
    }
    serializer = ClienteSerializer(data=data)
    assert serializer.is_valid()
    cliente = serializer.save()
    assert cliente.nombre == "Test Cliente"
