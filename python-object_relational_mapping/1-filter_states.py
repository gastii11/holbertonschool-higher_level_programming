#!/usr/bin/python3
"""Este módulo se conecta a una base de datos y lista todos los estados
cuyo nombre comienza con N"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    result = cur.fetchall()

    for i in result:
        print(i)

    cur.close()
    db.close()
