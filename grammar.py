import requests


def query(payload, api):
    carrier = dict(
        inputs=f"'{payload}' \nGrammar Corrected statement is:")
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": f"Bearer {api}"}
    response = requests.post(API_URL, headers=headers, json=carrier)
    return response.json()[0]["generated_text"]
