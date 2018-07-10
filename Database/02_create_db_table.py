# https://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "pytestdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exists using execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
