# test json inputs

import json
from pprint import pprint

with open('data.json') as data_file:
	data = json.load(data_file)

pprint(data)

# if only imported pprint then it will be pprint.pprint(data)