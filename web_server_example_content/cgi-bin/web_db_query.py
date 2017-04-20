#!/Users/john/anaconda/bin/python3
#
# web_db_query.py
# j.weible
#
# A brief example of a dynamic web page querying a MySQL database

# Measly docs for pymysql module https://pymysql.readthedocs.io/en/latest/
# But it's mostly compatible with the "MySqlDB" API, documented here:
#  http://mysql-python.sourceforge.net/MySQLdb.html
import pymysql
from os import environ
import cgi

def main():
    xhtml_start()

    data = get_http_query_string()
    if not data:
        data = {'search_field': 'Title',
                'search_text': '%Monty Python%'}
    xhtml_search_form(data)

    search_IMDB(data)

    xhtml_end()
    return


def search_IMDB(search: dict):
    """Connect to MySQL IMDB database,
    search for the term(s) specified,
    output results, and disconnect."""

    # Caveat: The simple method of getting a password below is
    # not super secure. But it is FAR better than putting the
    # password in the program code!

    # See if the password was set in my OS environment:
    db_password = environ['IMDB_password']
    if not db_password:
        print('database password missing.')

    # Open database connection to iSchool's MySQL
    db = pymysql.connect(host="cpanel.ischool.illinois.edu",
                         user="jweible_IMDB_ro",
                         passwd=db_password,
                         db="jweible_IMDB")

    # Create a cursor object. Instead of getting tuples for
    # query results, this option returns a list of dictionaries
    cursor = db.cursor(pymysql.cursors.DictCursor)

    if search['search_field'] == 'Title':
        value = search['search_text']
        print('<h1>Title search for', value, '</h1>')
        query = "select Title, ReleaseYear from production " + \
                "where Title like %s and isMovie = True"
    elif search['search_field'] == 'LastName':
        value = search['search_text']
        print('<h1>Actor or Director search for lastname of', value, '</h1>')
        query = "select FirstName, LastName from person " + \
                "where LastName like %s"
    else:
        print('<p>Search data missing or not understood.</p>')
        return

    # Execute the SQL query
    params = [value]  # put value(s) in a list
    # print('<p>Query is <code>', query, '</code><br />' +
    #       'and parameters are<code>', params, '</code></p>')
    cursor.execute(query, params)

    # Fetch all the rows into a tuple of tuples:
    results = cursor.fetchall()

    display_results(results)

    db.close()  # disconnect from database server
    return


def display_results(results: list):
    """Given a list of data rows (as dictionaries), display the results in XHTML format."""
    if not results:
        print('<p>No matching results found.</p>')
        return
    print('<table style="border: 2px;">')  # start html table
    print('\t<tr>')  # start html table row
    keys_sorted = sorted(results[0].keys())
    for key in keys_sorted:
        print('\t\t<th>' + key + '</th>')  # show column name in table header cell
    print('\t</tr>')  # close the html table row

    for row in results:
        print('\t<tr>')
        for key in keys_sorted:
            print('\t\t<td>', row[key], '</td>', sep='')  # show value in table data cell
        print('\t</tr>')
    print('</table>')  # close html table
    return

def get_http_query_string() -> dict:
    """Looks for key=value pair(s) on the URL (from the search form) """
    query_data = cgi.FieldStorage()

    data = {}
    for key in ['search_field', 'search_text']:
        if key in query_data.keys():
            data[key] = query_data[key].value
    return data


def xhtml_start():
    """Prints response header and other necessary XHTML document stuff."""

    # The next 2 lines tell the user's web browser the content is (X)HTML.
    print("Content-Type: text/html")  # HTML is following
    print()  # blank line indicates end of response headers

    print("""
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>A simple IMDB database search</title>
        <link rel="stylesheet" type="text/css" href="/simple.css" />
    </head>
    <body>
    """)
    return

def xhtml_search_form(data: dict):
    """Prints out a simple search form that re-submits to this same page.
    :param data lets the form input fields default to the previous settings."""
    print("""
    <form action="web_db_query.py" method="get">
        <div>
        <h2>Search:</h2>
        <select name="search_field">""")

    # Print out the <option> tags.  The conditional is to automatically select
    #  the same option that was used in the last search.

    if data['search_field'] == 'Title':
        print("""
            <option value='Title' selected='selected'>Title</option>
            <option value='LastName'>Actor or Director LastName</option>""")
    elif data['search_field'] == 'LastName':
        print("""
            <option value='Title'>Title</option>
            <option value='LastName' selected='selected'>Actor or Director LastName</option>""")

    print("""
        </select>
        <br />
        Enter the text to search for. (Use % for wildcard)""")

    print('<input name="search_text" type="text" size="60" value="{}"/>'.format(data['search_text']))
    print("""
            <input type="submit" />
        </div>
    </form>""")
    return

def xhtml_end():
    print('</body>\n</html>')
    return

main()
