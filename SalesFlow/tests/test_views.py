import pytest
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_clientes_list_authenticated():
    client = APIClient()
    client.login(username='testuser', password='testpassword')
    response = client.get('/api/clientes/')
    assert response.status_code == HTTP_200_OK

@pytest.mark.django_db
def test_clientes_list_unauthenticated():
    client = APIClient()
    response = client.get('/api/clientes/')
    assert response.status_code == HTTP_401_UNAUTHORIZED
