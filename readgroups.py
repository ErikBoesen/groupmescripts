import requests

TOKEN = input('Token: ')

def get_groups():
    response = requests.get('https://api.groupme.com/v3/groups?token=' + TOKEN)
    return response.json()['response']

groups = get_groups()
for group in groups:
    try:
        print(group.get('name', "NO NAME") + "\t\t" + group.get('share_url', "NO LINK"))
    except:
        print("Failed one")
