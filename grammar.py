import requests
import api


def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": f"Bearer {api.hf}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]


text = "I life here"
output = query({
    "inputs": f"{text} \nCorrect statement is:",
})
print(output)
