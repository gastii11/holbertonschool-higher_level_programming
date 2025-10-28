#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
