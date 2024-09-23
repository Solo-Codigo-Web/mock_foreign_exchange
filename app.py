import requests
from settings import API_FOREIGN_EXCHANGE


def convert_euros_to_dollar(amount: float) -> float:
    """
    Función para convertir euros a dolares.
    """
    # Llamada a una API para obtener el tipo de cambio EUR -> USD
    api_endpoint: str = "{}/EUR".format(API_FOREIGN_EXCHANGE)
    response = requests.get(api_endpoint)

    if response.status_code != 200:
        raise Exception("No se pudo obtener el tipo de cambio")

    data = response.json()

    # Obtenemos el tipo de cambio de EUR a USD
    rate = data["rates"]["USD"]

    # Devolvemos la cantidad en dólares
    return round(amount * rate, 2)
