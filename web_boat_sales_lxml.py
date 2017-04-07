# "Row-ing Boats For Sale"
# An example of using lxml to parse invalid HTML and extract data
# from the resulting document tree (DOM), mostly with XPath.
#
# J. Weible

import lxml.html
import re

# url = 'http://www.sailboatlistings.com/location/Michigan'

state = input('Enter the name of a state (e.g. Michigan) to search:')

# In the search URL below, the 'mh' key says how many results to return per page. Default is 100.
url = 'http://www.sailboatlistings.com/cgi-bin/saildata/db.cgi' \
              + '?db=default&sbltable=1&mh=100&uid=default&view_records=1&sb=5&so=descend&nh=1' \
              + '&state=' + state.strip()

# Fetch the url web page, and convert the response into an HTML document tree:
tree = lxml.html.parse(url)

title = tree.xpath('//title/text()')
print('Page title: ', title[0])

# Here's what one table row looks like in the (invalid) HTML from that web page:
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
    <td><a href="http://www.sailboatlistings.com/view/45613">Details</a></td>"""

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

# Here's an xpath that only extracts the links to detail pages:
# It works by finding a nested sequence of <tr>  <td> .. <a href...>
#  where the content (link url) in the href attribute contains the string '/view/'
#  and then matching (returning) only the href portion.
boat_detail_links = tree.xpath("//tr/td/a[contains(@href,'/view/')]/@href")
print(boat_detail_links)


# Here's an xpath that only extracts the prices:
# It works by finding a table cell with <a href...> having 'Details' as its text.
# Then it goes "up" the tree one level with /../ and then finds the 7th sibling <td>
# and returns the text it contains.
boat_prices = tree.xpath("//tr/td/a[text()='Details']/../following-sibling::td[7]/text()")
print(boat_prices)

# The problem with the approaches above in this case is that they're independent of
# each other. Thus, we can't be sure whether the matches we found for links (with IDs)
# belong to the same boats as the prices found.

# So the correct approach is to first locate where all these table rows are in the
# document tree and iterate through them to pull out all the data we want from each row,
# one at a time.

# The following xpath matches every table row that contains a link called "Details".
# Notice it finds the link, then backs "up" the tree 2 levels to stop on the <tr>:
boat_rows = tree.xpath("//tr/td/a[text()='Details']/../..")

# Now we can iterate through the boat_rows, searching each time within a
# different <tr>, containing one boat's data:

boats = []  # let's load the data into a list of dictionaries
for r in boat_rows:
    boat = {}

    detail_url = r.xpath("td[1]/a/@href")[0]  # href from 1st cell
    # Get the ID from the href url using a regex:
    boat['id'] = re.findall(r'/view/(\d+)', detail_url)[0]
    boat['length'] = r.xpath("td[2]/text()")[0]

    year = r.xpath("td[3]/text()")
    if year:
        boat['year'] = year[0]
    else:
        boat['year'] = ''

    boat['mfg'] = r.xpath("td[4]/a/text()")[0]

    model = r.xpath("td[5]/a/text()")
    if model:
        boat['model'] = model[0]
    else:
        boat['model'] = ''

    city = r.xpath("td[6]/a/text()")
    if city:
        boat['city'] = city[0]
    else:
        boat['city'] = ''

    boat['state'] = r.xpath("td[7]/text()")[0]
    boat['price'] = r.xpath("td[8]/text()")[0]

    print(boat)
    boats.append(boat)  # Add data from row into the list
