import requests

GROUP_ID = 48071223

bot_id = input("Bot ID: ")
while True:
    text = input("> ")
    r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": bot_id, "text": text})
