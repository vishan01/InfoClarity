import requests


def query(payload, api):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {api}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["summary_text"]
