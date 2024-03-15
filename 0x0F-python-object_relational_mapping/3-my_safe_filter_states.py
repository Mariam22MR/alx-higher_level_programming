#!/usr/bin/python3
""" Prints all rows in states table of database
with name that matches given argument and is safe from SQL injection """
import MySQLdb
from sys import argv


def main():
    """ Function not run when imported module """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    start = db.cursor()
    query = """SELECT * FROM states WHERE states.name = %s
            ORDER BY states.id"""
    start.execute(query, (argv[4],))
    rows = start.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
