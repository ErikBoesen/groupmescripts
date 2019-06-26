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
def post(path, data):
    requests.post(endpoint(path), data=data)

colleges = [
    'Benjamin Franklin',
    'Berkeley',
    'Benjamin Franklin',
    'Berkeley',
    'Branford',
    'Davenport',
    'Ezra Stiles',
    'Grace Hopper',
    'Jonathan Edwards',
    'Morse',
    'Pauli Murray',
    'Pierson',
    'Saybrook',
    'Silliman',
    'Timothy Dwight',
    'Trumbull',
]
for college in colleges:
    image_upload = requests.post('https://image.groupme.com/pictures?token=' + args.token, files={'file': open('shields/' + college.replace(' ', ''), 'rb')})
    if not image_upload.ok:
        break
    image_url = image_upload.json()['payload']['url']
    post('groups', {'name': 'Yale ' +  college + ' College 2023',
                    'share': True,
                    'image_url': image_url})
