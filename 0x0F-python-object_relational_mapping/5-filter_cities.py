#!/usr/bin/python3
"""
a script takes in the name of a state as an argument and lists all
cities of that state
Your script should take 4 arguments: mysql username, mysql password,
database name and state name
Results must be sorted in ascending order by cities.id
You can use only execute() once
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities WHERE cities.state_id\
                     = (SELECT states.id FROM states WHERE states.name = '{}'\
                     LIMIT 1) ORDER BY cities.id".format(sys.argv[4]))
    rows = c.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
    print(", ".join(new_list))
    c.close()
    db.close()
