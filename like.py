import requests
import argparse

GROUP_ID = 57639249
MY_ID = 41430499


parser = argparse.ArgumentParser(description='Analyze a GroupMe chat')
parser.add_argument('token', help='Your GroupMe developer token')
args = parser.parse_args()

def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + args.token
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']
def post(path):
    requests.post(endpoint(path))

group = get('groups/%d' % GROUP_ID)

message_id = 0
message_number = 0
while message_number < group['messages']['count']:
    params = {
        # Get maximum number of messages at a time
        'limit': 100,
    }
    if message_id:
        params['before_id'] = message_id
    messages = get('groups/%s/messages' % group['id'], params)['messages']
    for message in messages:
        message_number += 1

        text = message['text'] or ''
        if not (message['sender_id'] == MY_ID or MY_ID in message['favorited_by']):
            post('messages/%d/%s/like' % (GROUP_ID, message['id']))
            print('Liked: ' + text)

    message_id = messages[-1]['id']  # Get last message's ID for next request
    remaining = 100 * message_number / group['messages']['count']
    print('\r%.2f%% done' % remaining, end='')
