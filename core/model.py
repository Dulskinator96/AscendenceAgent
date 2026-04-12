import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_model(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    if response.status_code != 200:
        raise Exception(f"Model request failed: {response.text}")
    
    return response.json()["response"]