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