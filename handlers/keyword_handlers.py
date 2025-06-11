"""
Keyword Research Handlers
Handles all keyword-related MCP tool calls
"""

from typing import Dict, Any
from ..utils.http_client import make_api_request
from ..utils.response_utils import limit_response_size


class KeywordHandlers:
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url

    def handle_keywords(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle keywords tool call"""
        url = f"{self.api_base_url}/keywords"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "version": args.get("version", "1"),
            "email": api_key  # Using API key as email for compatibility
        }
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10)

    def handle_keywords_with_volumes(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle keywords with volumes tool call"""
        url = f"{self.api_base_url}/keywords-with-volumes"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "email": api_key  # Using API key as email for compatibility
        }
        if "limit" in args:
            data["limit"] = min(args["limit"], 10)  # Cap at 10 for MCP
        else:
            data["limit"] = 10  # Default limit for MCP
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10)

    def handle_search_volume(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle search volume tool call"""
        url = f"{self.api_base_url}/search-volume"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "keywords": args["keywords"][:10] if isinstance(args["keywords"], list) else args["keywords"],  # Limit input keywords
            "search_country": args["search_country"],
            "version": args.get("version", "1"),
            "email": api_key  # Using API key as email for compatibility
        }
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10)

    def handle_related_keywords(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle related keywords tool call"""
        url = f"{self.api_base_url}/related-keywords"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "email": api_key  # Using API key as email for compatibility
        }
        if "limit" in args:
            data["limit"] = min(args["limit"], 10)  # Cap at 10 for MCP
        else:
            data["limit"] = 10  # Default limit for MCP
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10)

    def handle_lsi(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle LSI tool call"""
        url = f"{self.api_base_url}/lsi"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "email": api_key  # Using API key as email for compatibility
        }
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10) 