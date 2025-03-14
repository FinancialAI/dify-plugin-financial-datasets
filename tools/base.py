from enum import Enum
from typing import Any
from urllib.parse import urljoin

import requests


class Endpoint(Enum):
    """
    An enumeration representing API endpoints.
    """

    COMPANY_FACTS = "/company/facts"
    CRYPTO_PRICES = "/crypto/prices"
    CRYPTO_SNAPSHOT = "/crypto/prices/snapshot"
    EARNINGS_PRESS_RELEASES = "/earnings/press-releases"
    FINAANCIAL_METRICS_HISTORICAL = "/financial-metrics"
    FINAANCIAL_METRICS_SNAPSHOT = "/financial-metrics/snapshot"
    FINANCIAL_STATEMENTS = "/financials"
    INSIDER_TRADES = "/insider-trades"
    INSTITUTIONAL_OWNERSHIP = "/institutional-ownership"


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
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(
            urljoin(BASE_URL, endpoint.value), params=params, headers=headers
        )
        # response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error sending request: {e}")
    except Exception as e:
        raise Exception(f"Error processing response: {e}")


def get_required_parameter(tool_parameters: dict[str, Any], parameter: str):
    """
    Checks if the specified parameter is present in the tool parameters.

    Args:
        tool_parameters (dict[str, Any]): A dictionary containing the parameters
            required for the tool.
        parameter (str): The name of the parameter to check.

    Raises:
        ValueError: If the specified parameter is missing from tool_parameters.
    """
    if parameter not in tool_parameters:
        raise ValueError(f"Missing required parameter: {parameter}")

    return tool_parameters[parameter]
