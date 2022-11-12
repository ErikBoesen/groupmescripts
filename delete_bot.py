import requests
import os

def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + os.environ['GROUPME_ACCESS_TOKEN']
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']
def post(path, params=None):
    return requests.post(endpoint(path), params=params)

bot_id = input('Bot ID to delete: ')
r = post('bots/destroy', params={'bot_id': bot_id})
print(r.json())
