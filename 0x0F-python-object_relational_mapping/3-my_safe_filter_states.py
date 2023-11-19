#!/usr/bin/python3
"""
this module takes an argument and displays all values in
the states table of the database where name matches the argyment
but safe from SQL injections this time
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    MY_USER, MY_PASS, MY_DB, MY_STATE = argv[1:]

    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cursor = db.cursor()
    command = "SELECT * FROM states WHERE name =BINARY %s ORDER BY id"

    cursor.execute(command, (MY_STATE,))
    query = cursor.fetchall()
    for row in query:
        print(row)

    cursor.close()
    db.close()
