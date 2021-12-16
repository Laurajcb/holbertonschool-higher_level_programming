#!/usr/bin/python3
"""
List all the state from a db hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "_main_":
    db = connect(host='localhots', port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FORM 'state'")
    row = cur.fetchall()
    for states in row:
        print(states)
    cur.close()
    db.close()
