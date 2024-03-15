#!/usr/bin/python3
""" Get all states from database with filter """
import MySQLdb
import sys


def main():
    """ Main function not executed when import module """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    start = db.cursor()
    start.execute("""SELECT * FROM states WHERE states.name LIKE BINARY 'N%'
                        ORDER BY states.id""")
    rows = start.fetchall()
    for row in rows:
        print(row)
    start.close()
    db.close()


if __name__ == "__main__":
    main()
