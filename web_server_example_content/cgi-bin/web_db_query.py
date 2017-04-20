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


def main():
    xhtml_start()

    data = {'Title': '%Monty Python%'}
    search_IMDB(data)

    xhtml_end()
    return


def search_IMDB(search_terms: dict):
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

    if 'Title' in search_terms.keys():
        value = search_terms['Title']
        print('<p>Title search for', value, '</p>')
        query = "select Title, ReleaseYear from production " + \
                "where Title like %s and isMovie = True"
        params = [value]  # put value(s) in a list
    else:
        print('<p>Search data missing or not understood.</p>')
        return

    # Execute the SQL command
    print('<p>Query is <code>', query, '</code><br />' +
          'and parameters are<code>', params, '</code></p>')
    cursor.execute(query, params)

    # Fetch all the rows into a tuple of tuples:
    results = cursor.fetchall()
    for row in results:
        print('<p>', row["Title"], '</p>')

    db.close()  # disconnect from server
    return


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
    </head>
    <body>
    """)
    return


def xhtml_end():
    print('</body>\n</html>')
    return

main()
