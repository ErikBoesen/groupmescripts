import requests
import argparse

MY_ID = 41430499


parser = argparse.ArgumentParser()
parser.add_argument('token', help='Your GroupMe developer token')
args = parser.parse_args()

def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + args.token
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']

colleges = [
        'Benjamin Franklin': '51337432/1P01Jawj',
        'Berkeley': '51337452/WS6dYrya',
        'Branford': '51337464/0DfxyBPh',
        'Davenport': '51337471/QydP3Uqp',
        'Ezra Stiles': '51337477/4SwHEUhM',
        'Grace Hopper': '51337487/NqXZODp7',
        'Jonathan Edwards': '51337498/t5Oq3QCc',
        'Morse': '51337503/ptRvZZoN',
        'Pauli Murray': '51337511/YNisIp1h',
        'Pierson': '51337516/umZfwuER',
        'Saybrook': '51337528/6wtXL5hD',
        'Silliman': '51337538/NuVpessh',
        'Timothy Dwight': '51337543/WU4U245f',
        'Trumbull': '51337553/VKFb0cmd',
]
from groupy.client import Client
client = Client.from_token(args.token)
results = {}
for college in colleges:
    print(college)
    image_upload = requests.post('https://image.groupme.com/pictures?token=' + args.token,
                                 files={'file': open('shields/' + college.replace(' ', '') + '.png', 'rb')})
    if not image_upload.ok:
        print('Image upload failed.')
        print(image_upload.text)
        break
    image_url = image_upload.json()['payload']['url']
    print(image_url)
    new_group = client.groups.create('Yale ' + college + ' College 2023', image_url=image_url, share=True)
    results[college] = new_group.share_url
    """
    creation = requests.post('https://api.groupme.com/v3/groups?token=' + args.token,
                             data={'name': 'Yale ' +  college + ' College 2023',
                                   'share': True,
                                   'image_url': image_url})
    if not creation.ok:
        print('Creation failed.')
        print(creation.text)
        break
    results[college] = creation.json()['share_url']
    """
print(results)
