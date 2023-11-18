#!/usr/bin/python3
"""
Lists all states from specified database
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    MY_USER, MY_PASS, MY_DB = argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, passwd=MY_PASS,
                         db=MY_DB, user=MY_USER)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
