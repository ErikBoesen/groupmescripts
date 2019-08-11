import requests
from datetime import date

GROUP_ID = 46649296

def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + os.environ['GROUPME_ACCESS_TOKEN']
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']
def post(path):
    requests.post(endpoint(path))

frequency = {}

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
        if not message['system']:
            d = date.fromtimestamp(message['timestamp'])
            if frequency.get(d):
                frequency[d] += 1
            else:
                frequency[d] = 1

    message_id = messages[-1]['id']  # Get last message's ID for next request
    remaining = 100 * message_number / group['messages']['count']
    if remaining > 5:
        break
    print('\r%.2f%% done' % remaining, end='')

print(frequency)
