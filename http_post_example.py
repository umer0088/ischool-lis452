import requests
import lxml.html

# StartPage is a privacy-centric search engine, and
# the search form using POST instead of GET method.

# So how do we figure out how to specify the query data in the request?
url = 'https://startpage.com/do/asearch'

# r = requests.get(url)

# POST to /do/asearch
# <input name="cat" value="web" type="hidden">
# <input name="cmd" value="process_search" type="hidden">
# <input name="language" value="english" type="hidden">
# <input name="engine0" value="v1all" type="hidden">
# <input id="query5" name="query" onchange="checkContent();" onkeydown="checkContent();" onkeyup="checkContent();" type="text">
# <input id="abp" name="abp" value="-1" type="hidden">
# <input name="t" value="air" type="hidden">
# <input id="nj" name="nj" value="0" type="hidden">

query_string = input("What do you want to search for?")

key_pairs = {'cat': 'web',
        'cmd': 'process_search',
        'language': 'english',
        'engine0': 'v1all',
        'abp': '-1',
        't': 'air',
        'nj': '0',
        'query': query_string}

r = requests.post(url, data=key_pairs)

if not r.ok:
    print('Had an error')
    exit()

print('Response Header:')
for i in r.headers.keys():
    print(i + ' = ' + r.headers[i])

# print(r.text)

tree = lxml.html.fromstring(r.text)

title = tree.xpath('//title/text()')
print('Page title: ', title[0])

# This XPath extracts just the "title" text from each search result we got:
results = tree.xpath("//ol[contains(@class,'web_regular_results')]//span[contains(@class,'result_url_heading')]/text()")
for i in range(len(results)):
    print(i + 1, ': ', results[i])

