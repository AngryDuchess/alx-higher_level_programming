#!/usr/bin/python3
"""
this module takes an argument and displays all values in
the states table of the database where name matches the argyment
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    MY_USER, MY_PASS, MY_DB, MY_STATE = argv[1:]

    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cursor = db.cursor()
    command = "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id\
            ".format(MY_STATE)

    cursor.execute(command)
    query = cursor.fetchall()
    for row in query:
        print(row)

    cursor.close()
    db.close()
