#!/usr/bin/python3
"""
lists all states with name starting with an N from a specified database
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    MY_USER, MY_PASS, MY_DB = argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
