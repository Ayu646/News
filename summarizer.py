
import requests

def summarize_text(text, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a news summarizer."},
            {"role": "user", "content": text}
        ],
        "temperature": 0.3,
    }
    response = requests.post(url, headers=headers, json=data)
    summary = response.json()["choices"][0]["message"]["content"]
    return summary
