# https://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "pytestdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Stephen', 'Fleming', 25, 'M', 20000)"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
