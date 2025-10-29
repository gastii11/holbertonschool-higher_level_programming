#!/usr/bin/python3
"""Script que lista todos los estados"""
import sys
import MySQLdb


def list_states_safe():
    """
    Conecta a la base de datos MySQL y ejecuta una consulta SELECT segura,
    filtrando los estados por nombre.
    """
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = None
    cursor = None

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=db_name)

        cursor = db.cursor()

        sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cursor.execute(sql_query, (state_name,))

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f'Error al conectar o ejecutar la consulta: {e}' file=sys.stderr)
        sys.exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    list_states_safe()
