import requests
import argparse

GROUP_ID = 46649296
MY_ID = 41430499
TARGET_ID = 31870258


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
occurrences = {}
num_words = 0
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
            text = text.lower()
            text = ''.join([c for c in text if c.isalpha() or c == ' '])
            words = text.split()
            num_words += len(words)
            for word in words:
                if word not in occurrences:
                    occurrences[word] = 0
                occurrences[word] += 1

    message_id = messages[-1]['id']  # Get last message's ID for next request
    remaining = 100 * message_number / group['messages']['count']
    print('\r%.2f%% done' % remaining, end='')

print('\nParsed %d messages.' % message_number)

with open('words.csv', 'w') as f:
    f.write('word,occurrences,frequency\n')
    for word in occurrences:
        f.write('%s,%d,%f\n' % (word, occurrences[word], occurrences[word] / num_words))
