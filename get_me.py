import requests
import json

TOKEN = input('Token: ')

def get_me():
    response = requests.get('https://api.groupme.com/v3/users/me?token=' + TOKEN)
    return response.json()['response']

me = get_me()
print(me)
