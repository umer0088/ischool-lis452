import requests
import re

state = input('Enter the name of a state (e.g. Michigan) to search:')
limit = int(input('How many records do you want maximum. Expects 100, 200, etc.?'))

# Simple url = 'http://www.sailboatlistings.com/location/Michigan'

# In the URL below, the 'mh' key says how many results to return per page. Default is 100.
url = 'http://www.sailboatlistings.com/cgi-bin/saildata/db.cgi'
# state = 'Michigan'
kv_pairs = {'db': 'default', 'sbltable': 1,
            'uid': 'default', 'view_records': 1,'sb': 5,
            'so': 'descend', 'nh':1,
            'mh': limit, 'state': state}
state_page = requests.get(url, kv_pairs)  # Fetch the web page

print('Complete URL requested was:', state_page.url)
print('Response Headers were:\n', state_page.headers)

state_html = state_page.text

# print(state_html)

# First let's start with what we know about regex to pull out some bits from
# this HTML response:

# A very simple example, because <title> can only occur once in a page:
title = re.findall('<title>(.*?)</title>', state_html)[0]
print('The page title is:', title)

# Here's what one table row looks like in HTML:
"""
<TR>
    <td><a href="http://www.sailboatlistings.com/view/45613">Details</a></td>
    <td background="/tb/b1.jpg">48</font></td>
    <td background="/tb/b2.jpg">2013</td>
    <td background="/tb/b3.jpg"><a href="/cgi-bin/saildata/db.cgi?db=default&uid=default&manufacturer=Beneteau&view_records=1&sb=date&so=descend">Beneteau</a></td>
    <td background="/tb/b4.jpg"><a href="/cgi-bin/saildata/db.cgi?db=default&uid=default&model=48 Oceanis&view_records=1&sb=date&so=descend">48 Oceanis</a></td>
    <td background="/tb/b5.jpg"><a href="/cgi-bin/saildata/db.cgi?db=default&uid=default&city=Muskegon&view_records=1&sb=date&so=descend">Muskegon</a></td>
    <td background="/tb/b6.jpg">Michigan</td>
    <td background="/tb/b7.jpg" align="right">$ 455,000</td>
    <td><a href="http://www.sailboatlistings.com/view/45613">Details</a></td>  """

# How to extract selected boat data from the table?
# They are in an HTML table, with 1 row per boat.
# Cell 1: link to another web page with the details
# Cell 2: Length in feet or feet and inches.
# Cell 3: Year made
# Cell 4: Manufacturer
# Cell 5: Model
# Cell 6: City/port where it's supposedly located
# Cell 7: State of listing/ownership
# Cell 8: Listed price
# Cell 9: A duplicate link to details, but it may contain a picture.
listings = re.findall(
        r"""<tr>\s*?   # match start of a table row and spaces
            # match a link to a detail view page and capture item number:
            <td><a\ href="http://www\.sailboatlistings\.com/view/(\d+)".+?</td>
            .*?<td[^>]*>(.*?)(?:</font>)</td>  # boat length, excluding the invalid </font> tag
            (?:.*?<td[^>]*>){6} # match 7 more <td...> tags without capturing
            (.*?)</td>""",      # capture everything inside the current <td> tag
        state_html, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE | re.VERBOSE)
print('The data found are:', listings)

for t in listings:
    print('{:6} {:10} {:10}'.format(t[0], t[1], t[2]))

# Even with the power of regexes, it can become very awkward and unpredictable for
# extracting specific pieces of XML or HTML, so we have specialized parsers for XML.
#
#  See next example...
