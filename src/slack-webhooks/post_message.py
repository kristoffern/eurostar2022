import requests
import os

SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK')

headers = {'Content-type': 'application/json'}

requests.post(WEBHOOK, headers=headers, json={"text":"Hello, World!"})
