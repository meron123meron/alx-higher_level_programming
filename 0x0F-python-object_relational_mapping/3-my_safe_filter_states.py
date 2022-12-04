#!/usr/bin/python3
"""
The same as task 2 But this time, write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name=%s\
              ORDER BY states.id ASC".format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
