"""
    Mailgun Demo

    A short demo showing how Mailgun can be used to send emails directly from Python.
    To try the code out yourself, register a free account at https://www.mailgun.com/

    You can use the sandbox domain created out of the box and send emails to the
    registered email address you used for the account.
    
    Replace the sandbox domain in the code below
    ("https://api.mailgun.net/v3/[YOUR_SANDBOX_DOMAIN].mailgun.org/messages",)
    and then set the environmental variable MAILGUN_KEY with the API
    you got in your initial email or find it under your Mailgun account.
"""


import requests
import os

API_KEY = os.getenv('MAILGUN_KEY')
print(API_KEY)

result = requests.post(
        "https://api.mailgun.net/v3/sandbox90d07f3bc51246b09192415d5231084e.mailgun.org/messages",
        auth=("api", API_KEY),
        data={"from": "Excited User <mailgun@northerntest.se>",
              "to": ["tester@northerntest.se"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

print(result.text)