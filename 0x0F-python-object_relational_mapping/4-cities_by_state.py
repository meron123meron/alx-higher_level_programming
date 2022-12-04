#!/usr/bin/python3
"""
 a script that lists all cities from the database hbtn_0e_4_usa
 """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              LEFT JOIN states ON  states.id = cities.state_id\
              ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
