import requests

# StartPage is a privacy-centric search engine, and
# the search form using POST instead of GET method.

# So how do we figure out how to specify the query data in the request?
url = 'https://startpage.com/'

r = requests.get(url)
if not r.ok:
    print('Had an error')
    exit()

print('Response Header:')
for i in r.headers.keys():
    print(i + ' = ' + r.headers[i])
