import os
import requests
from datetime import date
from collections import OrderedDict


GROUP_ID = 46649296

def endpoint(path):
    return 'https://api.groupme.com/v3/' + path + '?token=' + os.environ['GROUPME_ACCESS_TOKEN']
def get(path, params=None):
    return requests.get(endpoint(path), params=params).json()['response']
def post(path):
    requests.post(endpoint(path))

frequency = OrderedDict()

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
            d = date.fromtimestamp(message['created_at'])
            if frequency.get(d):
                frequency[d] += 1
            else:
                frequency[d] = 1

    message_id = messages[-1]['id']  # Get last message's ID for next request
    remaining = 100 * message_number / group['messages']['count']
    print('\r%.2f%% done' % remaining, end='')

print(frequency)
with open('usage.csv', 'w') as f:
    f.write('date,messages\n')
    for d, messages in reversed(list(frequency.items())):
        f.write(d.strftime('%Y-%m-%d') + ',' + str(messages) + '\n')
