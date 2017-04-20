#!/Users/john/anaconda/bin/python3
#
# mysql_simple_query.py
# j.weible
#
# A brief example of connecting and querying a MySQL database
#  located on the iSchool server

# Measly docs for pymysql module https://pymysql.readthedocs.io/en/latest/
# But it's mostly compatible with the "MySqlDB" API, documented here:
#  http://mysql-python.sourceforge.net/MySQLdb.html
import pymysql
from os import environ

# Caveat: The simple method of sending a password below is
# not very secure. But it is still FAR better than putting the
# password in the program code!!

# See if the password was set in my OS environment:
db_password = environ['IMDB_password']
if not db_password:
    db_password = input('Enter MySQL password:')

# Open database connection
db = pymysql.connect(host="cpanel.ischool.illinois.edu",
                     user="jweible_IMDB_ro",
                     passwd=db_password,
                     db="jweible_IMDB")

# Create a cursor object. Instead of getting tuples for
# query results, this option returns a list of dictionaries
cursor = db.cursor(pymysql.cursors.DictCursor)

# Prepare SQL query to search for records in the database:
query = """
select Title, ReleaseYear, ProdID from production
    where title like %s and isMovie = True
"""
params = ['%star wars%']

# Execute the SQL command
cursor.execute(query, params)

# Fetch all the rows into a tuple of tuples:
results = cursor.fetchall()
for row in results:
    print(row)

# disconnect from server
db.close()
