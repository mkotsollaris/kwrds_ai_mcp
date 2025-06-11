"""
AI Handlers
Handles AI-powered keyword research and content generation MCP tool calls
"""

from typing import Dict, Any
from ..utils.http_client import make_api_request
from ..utils.response_utils import limit_response_size, truncate_string_fields


class AIHandlers:
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url

    def handle_ai(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle AI tool call"""
        url = f"{self.api_base_url}/ai"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "prompt": args["prompt"],
            "email": api_key  # Using API key as email for compatibility
        }
        response = make_api_request(url, headers, data)
        limited_response = limit_response_size(response, max_items=10)
        return truncate_string_fields(limited_response, max_length=1000)

    def handle_ai_content(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle AI content generation tool call"""
        url = f"{self.api_base_url}/ai/content"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "prompt": args["prompt"],
            "email": api_key  # Using API key as email for compatibility
        }
        if "title" in args:
            data["title"] = args["title"]
        if "description" in args:
            data["description"] = args["description"]
        response = make_api_request(url, headers, data)
        limited_response = limit_response_size(response, max_items=10) 
        return truncate_string_fields(limited_response, max_length=1000) 