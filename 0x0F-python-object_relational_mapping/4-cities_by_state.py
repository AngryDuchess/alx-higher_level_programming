#!/usr/bin/python3
"""
lists all cities from the database specified
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    MY_USER, MY_PASS, MY_DB = argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cursor = db.cursor()
    command = """SELECT cities.id, cities.name, states.name FROM cities
               INNER JOIN states
               ON cities.state_id = states.id
               ORDER BY id"""
    cursor.execute(command)
    query = cursor.fetchall()

    for row in query:
        print(row)
    cursor.close()
    db.close()
