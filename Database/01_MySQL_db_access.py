# https://www.tutorialspoint.com/python/python_database_access.htm

"""
Performing Transactions
Transactions are a mechanism that ensures data consistency. Transactions have the following four properties −
1. Atomicity − Either a transaction completes or nothing happens at all.
2. Consistency − A transaction must start in a consistent state and leave the system in a consistent state.
3. Isolation − Intermediate results of a transaction are not visible outside the current transaction.
4. Durability − Once a transaction was committed, the effects are persistent, even after a system failure.
The Python DB API provides two methods to either commit or rollback a transaction.
"""

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "root", "pytestdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()
