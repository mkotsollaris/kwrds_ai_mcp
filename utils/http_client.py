"""
HTTP client utility for making API requests
"""

import requests
from typing import Dict, Any, Optional

def make_api_request(url: str, headers: Dict[str, str], data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None, method: str = "POST") -> Dict[str, Any]:
    """Make HTTP API requests with proper error handling"""
    try:
        # Convert any non-string values in data to strings to avoid header issues
        if data:
            data = convert_params_to_strings(data)
        if params:
            params = convert_params_to_strings(params)
            
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=params, timeout=30)
        else:
            response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            error_text = response.text
            raise Exception(f"API request failed with status {response.status_code}: {error_text}")
            
    except requests.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Error making API request: {str(e)}")

def convert_params_to_strings(params: Dict[str, Any]) -> Dict[str, Any]:
    """Convert all parameter values to strings to avoid header type issues"""
    converted = {}
    for key, value in params.items():
        if isinstance(value, (int, float)):
            converted[key] = str(value)
        elif isinstance(value, list):
            # Convert lists to comma-separated strings
            converted[key] = ','.join(str(item) for item in value)
        elif isinstance(value, bool):
            converted[key] = str(value).lower()
        else:
            converted[key] = str(value) if value is not None else ""
    return converted
