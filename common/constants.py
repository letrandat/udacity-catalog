import json

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
