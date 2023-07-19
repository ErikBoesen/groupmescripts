import requests
import json

TOKEN = input('Token: ')

def get_groups():
    response = requests.get('https://api.groupme.com/v3/groups?omit=memberships&token=' + TOKEN)
    return response.json()['response']

groups = get_groups()
with open('groups.json', 'w') as f:
    json.dump(groups, f, indent=4)
