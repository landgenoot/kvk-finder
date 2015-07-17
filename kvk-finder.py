#!/usr/bin/env python

import requests
import re
import sys

def most_common(lst):
    return max(set(lst), key=lst.count)

args = sys.argv
args[0] = ''
keyword = "%20".join(args)

url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + keyword + "%20kvk&as_nlo=10000000&as_nhi=99999999"

r = requests.get(url)

a = r.json()
results = a[u'responseData'][u'results']

kvks = []
for result in results:
    numbers = re.findall(r'\d+', result[u'content'].encode('utf-8'))
    kvks = kvks + [i for i in numbers if len(i) == 8]
print most_common(kvks)
