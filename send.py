from groupy import Client
import os

GROUP_ID = 48071223


client = Client.from_token(os.environ["GROUPME_ACCESS_TOKEN"])
group = client.groups.get(id=GROUP_ID)
group.leave()
while True:
    group.post(text=input("> "))
