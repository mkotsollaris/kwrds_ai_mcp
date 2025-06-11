"""
HTTP client utility for making API requests
"""

import requests
from typing import Dict, Any, Optional

def make_api_request(method: str, url: str, headers: Dict[str, str], data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make HTTP API requests with proper error handling"""
    try:
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
