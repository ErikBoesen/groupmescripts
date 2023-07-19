import requests
import os

TOKEN = os.environ['GROUPME_ACCESS_TOKEN']

GROUP_ID = 65861954

JOIN_URL = 'https://groupme.com/join_group/'


def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + TOKEN
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']
def post(path, data={}):
    return requests.post(endpoint(path), data={})

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

        if message['sender_type'] == 'user':
            text = message['text'] or ''
            if JOIN_URL in text:
                print(message['text'])

    message_id = messages[-1]['id']  # Get last message's ID for next request
    remaining = 100 * message_number / group['messages']['count']
    #print('\r%.2f%% done' % remaining, end='')

print('\nParsed %d messages.' % message_number)
