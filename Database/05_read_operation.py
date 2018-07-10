# https://www.tutorialspoint.com/python/python_database_access.htm

"""
You can use either fetchone() method to fetch single record or fetchall() to fetch multiple values from a database table.
fetchone() − It fetches the next row of a query result set. A result set is an object that is returned when a cursor object
is used to query a table.
fetchall() − It fetches all the rows in a result set. If some rows have already been extracted from the result set, then
it retrieves the remaining rows from the result set.
rowcount − This is a read-only attribute and returns the number of rows that were affected by an execute() method.
"""

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "pytestdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (24000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # Now print fetched result
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fecth data")

# disconnect from server
db.close()
