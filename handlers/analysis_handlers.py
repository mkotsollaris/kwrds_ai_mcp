"""
Analysis Handlers
Handles SERP analysis, URL rankings, and PAA-related MCP tool calls
"""

from typing import Dict, Any
from utils.http_client import make_api_request
from utils.response_utils import limit_response_size


class AnalysisHandlers:
    def __init__(self, api_base_url: str, paa_base_url: str):
        self.api_base_url = api_base_url
        self.paa_base_url = paa_base_url

    def handle_serp(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle SERP tool call"""
        url = f"{self.api_base_url}/serp"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "search_question": args["search_question"],
            "search_country": args["search_country"],
            "volume": args.get("volume", 0),
            "email": api_key  # Using API key as email for compatibility
        }
        response = make_api_request(url, headers, data)
        return limit_response_size(response, max_items=10)

    def handle_serp_detailed(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle detailed SERP analysis tool call"""
        url = f"{self.api_base_url}/serp-detailed"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "url": args["url"],
            "email": api_key  # Using API key as email for compatibility
        }
        return make_api_request(url, headers, data)

    def handle_url_rankings(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle URL rankings tool call"""
        url = f"{self.api_base_url}/url-rankings"
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
        data = {
            "url": args["url"],
            "search_country": args["search_country"],
            "email": api_key  # Using API key as email for compatibility
        }
        return make_api_request(url, headers, data)

    def handle_paa(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle PAA tool call"""
        url = f"{self.paa_base_url}/people-also-ask"
        headers = {"X-API-KEY": api_key}
        params = {
            "keyword": args["keyword"],
            "search_country": args["search_country"],
            "search_language": args["search_language"],
            "X-API-KEY": api_key
        }
        response = make_api_request(url, headers, params=params, method="GET")
        return limit_response_size(response, max_items=10)

    def handle_paa_ai(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle PAA AI tool call - AI-powered analysis of People Also Ask questions"""
        try:
            # Prepare the payload for the /paa-ai endpoint
            payload = {
                "search_question": args.get("search_question", ""),
                "search_country": args.get("search_country", "us"),
                "question": args.get("question", ""),
                "email": args.get("email", ""),
                "prompt": args.get("prompt", "detailed")
            }
            
            # Make request to the /paa-ai endpoint
            url = f"{self.api_base_url}/paa-ai"
            headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
            response = make_api_request(url, headers, payload)
            return response
            
        except Exception as e:
            return {
                "error": f"Failed to get PAA AI analysis: {str(e)}",
                "search_question": args.get("search_question", ""),
                "question": args.get("question", "")
            }

    def handle_usage_count(self, args: Dict[str, Any], api_key: str) -> Dict[str, Any]:
        """Handle usage count requests"""
        try:
            url = f"{self.api_base_url}/usage_count"
            headers = {
                "Accept": "application/json",
                "X-API-KEY": api_key
            }
            result = make_api_request(url, headers, method="GET")
            return result
            
        except Exception as e:
            raise Exception(f"Failed to get usage count: {str(e)}") 