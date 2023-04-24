import requests

TOKEN = input('Token: ')

def get_bots():
    response = requests.get('https://api.groupme.com/v3/bots?token=' + TOKEN)
    return response.json()['response']

bots = get_bots()
for bot in bots:
    try:
        print(bot.get('name', "NO NAME") + "\t\t" + bot.get('share_url', "NO LINK"))
    except:
        print("Failed one")
