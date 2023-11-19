#!/usr/bin/python3
"""
lists all cities associated to a state name passed
as an argument to the script.
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    MY_USER, MY_PASS, MY_DB, MY_STATE = argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cursor = db.cursor()
    command = """SELECT cities.name FROM cities
              INNER JOIN states ON cities.state_id=states.id
              WHERE states.name = %s
              ORDER BY cities.id"""
    cursor.execute(command, (MY_STATE,))
    query = cursor.fetchall()

    found_cities = []
    for row in query:
        found_cities.extend(row)
    print(', '.join(found_cities))
    cursor.close()
    db.close()
