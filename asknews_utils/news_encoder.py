import json
from datetime import datetime
from typing import Any, Dict, List
from uuid import UUID


class NewsJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle special types"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        if hasattr(obj, '__dict__'):
            return self._clean_dict(obj.__dict__)
        return str(obj)

    def _clean_dict(self, d):
        """Clean dictionary by removing None values and private attributes"""
        return {k: v for k, v in d.items() if not k.startswith('_') and v is not None}


def convert_to_json(data: Any) -> Dict:
    """Convert objects to JSON-compatible dictionary"""
    if isinstance(data, list):
        return [convert_to_json(item) for item in data]

    if hasattr(data, '_asdict'):  # Handle namedtuple-like objects
        data = data._asdict()

    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if key.startswith('_') or value is None:
                continue

            if isinstance(value, (list, tuple)):
                result[key] = convert_to_json(value)
            elif isinstance(value, (dict, object)) and hasattr(value, '__dict__'):
                result[key] = convert_to_json(value.__dict__)
            elif isinstance(value, UUID):
                result[key] = str(value)
            elif isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result

    if hasattr(data, '__dict__'):
        return convert_to_json(data.__dict__)

    return str(data)


def extract_search_response_data(data):
    """Extract data from SearchResponse object or string representation"""
    if isinstance(data, str):
        # Handle string representation
        if "SearchResponseDictItem" in data:
            # Extract the list part from the string
            start = data.find("[")
            end = data.rfind("]")
            if start != -1 and end != -1:
                data = eval(data[start:end + 1])

    # Handle SearchResponse object
    if hasattr(data, 'as_dicts'):
        return data.as_dicts
    elif isinstance(data, tuple):
        # Handle tuple representation
        for item in data:
            if isinstance(item, list):
                return item
            elif isinstance(item, str) and "SearchResponseDictItem" in item:
                return extract_search_response_data(item)

    return data


def create_json_response(data: Any) -> str:
    """Create a formatted JSON response"""
    # Extract the actual data
    articles_data = extract_search_response_data(data)

    if not articles_data:
        return json.dumps({
            "status": "error",
            "message": "Could not extract articles data",
            "count": 0,
            "articles": []
        }, indent=2)

    response = {
        "status": "success",
        "count": len(articles_data),
        "articles": convert_to_json(articles_data)
    }

    return json.dumps(response, indent=2, ensure_ascii=False, cls=NewsJSONEncoder)
