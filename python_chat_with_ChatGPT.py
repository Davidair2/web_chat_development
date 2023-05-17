import requests
import json

def get_response(prompt):
    url = 'https://api.openai.com/v1/engines/text-davinci-002/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer YOUR_APIKEY',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 60,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

response = get_response("Is 'fuckyou' a destination or something about travel? please only answer with yes or no")
print(response['choices'][0]['text'].strip())
