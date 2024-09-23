import pytest
from unittest.mock import patch
from app import convert_euros_to_dollar


@patch('requests.get')
def test_convert_euros_to_dollars(mock_get):
    """
    Prueba unitaria para convertir euros a dólares
    """
    # Simulamos la respuesta de la API con un tipo de cambio ficticio
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "rates": {
            "USD": 1.15  # Ejemplo: 1 EUR = 1.15 USD
        }
    }
    amount: float = 100  # cantidad de euros
    expected_result: float = 115.0  # resultado esperado
    result: float = convert_euros_to_dollar(amount)

    # Verificar que el resultado sea el esperado (100 EUR * 1.15 = 115 USD)
    assert result == expected_result


@patch('requests.get')
def test_convert_euros_to_dollars_error_api(mock_get):
    """
    Prueba unitaria para simular un fallo en la API
    """
    # Simulamos un error de la API (HTTP Code 500)
    mock_get.return_value.status_code = 500

    # Ejecutar la función y verificar que se lanza una excepción
    with pytest.raises(Exception, match="No se pudo obtener el tipo de cambio"):
        convert_euros_to_dollar(100)
