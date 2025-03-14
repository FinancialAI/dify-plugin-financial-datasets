from enum import Enum
from typing import Any
from urllib.parse import urljoin

import requests


class Endpoint(Enum):
    """
    An enumeration representing API endpoints.
    """

    COMPANY_FACTS = "/company/facts"


BASE_URL = "https://api.financialdatasets.ai/"


def query(credentials: dict[str, Any], endpoint: Endpoint, params: dict):
    """
    Sends a GET request to the specified endpoint with the provided credentials and parameters.

    Args:
        credentials (dict[str, Any]): A dictionary containing the API credentials.
            Must include the key "financial_datasets_api_key".
        endpoint (Endpoint): The endpoint to which the request will be sent.
            Should be an instance of the `Endpoint` enum.
        params (dict): A dictionary of query parameters to include in the request.

    Returns:
        str: The response text from the API.

    Raises:
        Exception: If there is an error sending the request or processing the response.
    """
    try:
        headers = {
            "X-API-KEY": credentials["financial_datasets_api_key"],
            "Content-Type": "application/json",
        }
        response = requests.get(
            urljoin(BASE_URL, endpoint.value), params=params, headers=headers
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error sending request: {e}")
    except Exception as e:
        raise Exception(f"Error processing response: {e}")
