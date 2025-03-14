from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.base import Endpoint, query


class CompanyFactsTool(Tool):
    """
    A tool for retrieving company facts based on a given ticker symbol.

    Methods:
        _invoke(tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
            Executes the tool by querying company facts for the specified ticker symbol.

    Raises:
        ValueError: If the required "ticker" parameter is missing.

    Example:
        tool = CompanyFactsTool()
        tool_parameters = {"ticker": "AAPL"}
        response = tool._invoke(tool_parameters)
    """

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        Invokes the tool with the provided parameters and yields a response message.

        Args:
            tool_parameters (dict[str, Any]): A dictionary containing the parameters
                required for the tool. Must include the "ticker" key.

        Yields:
            ToolInvokeMessage: A message containing the response from the query.

        Raises:
            ValueError: If the "ticker" parameter is missing from tool_parameters.
        """

        ticker = tool_parameters.get("ticker")
        if not ticker:
            raise ValueError("Missing required parameter: ticker")

        resp = query(
            credentials=self.runtime.credentials,
            endpoint=Endpoint.COMPANY_FACTS,
            params={"ticker": ticker},
        )
        yield self.create_text_message(resp)
