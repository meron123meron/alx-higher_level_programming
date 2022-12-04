#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Results must be sorted in ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
