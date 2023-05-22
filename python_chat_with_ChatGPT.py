import requests
import json


def get_response(prompt):
    url = 'https://api.openai.com/v1/engines/text-davinci-002/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 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',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 60,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()