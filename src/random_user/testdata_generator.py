"""
	Example showing how to use the site randomuser.me to fetch random 
	test persons. Then store the retrieved testpersons in a locally available 
	json file. 
"""

from pprint import pprint
import requests
import json

data = dict()
data['results'] = []

f = open('testdata.json', 'w')


for _ in range(0,3):

	result = requests.get("https://randomuser.me/api/")
	person = result.json()['results'][0]

	data['results'].append(person)

pprint(data)
json.dump(data, f, indent=4)
f.close()

fr = open('testdata.json', 'r')

persons = json.load(fr)

pprint(persons)