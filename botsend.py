import requests

with open("bot_ids.txt", "r") as f:
    bot_ids = f.read().splitlines()

while True:
    text = input("> ")
    for bot_id in bot_ids:
        print("Sending to " + bot_id + "...", end="")
        r = requests.post("https://api.groupme.com/v3/bots/post", json={"bot_id": bot_id, "text": text})
        print(" done.")
