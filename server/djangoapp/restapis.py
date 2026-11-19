import os
from urllib.parse import quote

import requests

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """GET <backend_url><endpoint>. Returns parsed JSON, or None if the backend is unreachable."""
    try:
        response = requests.get(backend_url + endpoint, params=kwargs, timeout=10)
        return response.json()
    except (requests.RequestException, ValueError) as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """Call the sentiment analyzer. Falls back to 'neutral' if it is unreachable."""
    request_url = sentiment_analyzer_url.rstrip('/') + "/analyze/" + quote(text, safe='')
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except (requests.RequestException, ValueError) as err:
        print(f"Network exception occurred: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """POST a review to the backend. Returns parsed JSON, or None on failure."""
    try:
        response = requests.post(backend_url + "/insert_review", json=data_dict, timeout=10)
        return response.json()
    except (requests.RequestException, ValueError) as err:
        print(f"Network exception occurred: {err}")
        return None
