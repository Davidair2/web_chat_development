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

def check_response(prompt, response):
    messages = prompt + " " + response
    messages += " Do the previous sentences relate to travel, food or accommodation? Only answer yes or no"
    GPT_response = get_response(messages)
    checked_msg = GPT_response['choices'][0]['text']
    if checked_msg[-2:] == 'es':
        return True
    elif checked_msg[-1:] == 'o':
        return False
