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
    creation = requests.post('https://api.groupme.com/v3/groups?token=' + args.token,
                             data={'name': 'Yale ' +  college + ' College 2023',
                                   'share': True,
                                   'image_url': image_url})
    if not creation.ok:
        print('Creation failed.')
        print(creation.text)
        break
    results[college] = creation.json()['share_url']
print(results)
