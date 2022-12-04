#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched
You must use format to create the SQL query with the user input
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name\
              LIKE BINARY `name` = '{}'".format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
