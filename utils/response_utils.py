"""
Response utilities for limiting payload sizes
"""

from typing import Dict, Any


def limit_response_size(response: Dict[str, Any], max_items: int = 10) -> Dict[str, Any]:
    """
    Limit the size of API responses to prevent hitting Claude conversation limits
    
    Args:
        response: The API response dictionary
        max_items: Maximum number of items to return for arrays/lists
    
    Returns:
        Limited response dictionary
    """
    if not isinstance(response, dict):
        return response
    
    limited_response = {}
    
    for key, value in response.items():
        if isinstance(value, list) and len(value) > max_items:
            # Limit arrays to max_items and add a note about truncation
            limited_response[key] = value[:max_items]
            limited_response[f"{key}_truncated"] = True
            limited_response[f"{key}_total_count"] = len(value)
            limited_response[f"{key}_showing"] = max_items
        elif isinstance(value, dict):
            # Recursively limit nested dictionaries
            limited_response[key] = limit_response_size(value, max_items)
        else:
            # Keep other values as-is
            limited_response[key] = value
    
    return limited_response


def truncate_string_fields(response: Dict[str, Any], max_length: int = 500) -> Dict[str, Any]:
    """
    Truncate long string fields to prevent oversized responses
    
    Args:
        response: The API response dictionary  
        max_length: Maximum length for string fields
    
    Returns:
        Response with truncated strings
    """
    if not isinstance(response, dict):
        return response
    
    truncated_response = {}
    
    for key, value in response.items():
        if isinstance(value, str) and len(value) > max_length:
            truncated_response[key] = value[:max_length] + "... [truncated]"
        elif isinstance(value, dict):
            truncated_response[key] = truncate_string_fields(value, max_length)
        elif isinstance(value, list):
            truncated_response[key] = [
                truncate_string_fields(item, max_length) if isinstance(item, dict) 
                else (item[:max_length] + "... [truncated]" if isinstance(item, str) and len(item) > max_length else item)
                for item in value
            ]
        else:
            truncated_response[key] = value
    
    return truncated_response 