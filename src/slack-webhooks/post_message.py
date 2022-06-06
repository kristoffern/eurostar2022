import requests
import os

SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK')

headers = {'Content-type': 'application/json'}

requests.post('https://hooks.slack.com/services/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', headers=headers, json={"text":"Hello, World!"})
