#!/usr/bin/python3
"""
List all the state from a db hbtn_0e_0_usa
"""


from MySQLdb import _mysql
from sys import argv


if __name__ == "__main__":
    db = MySQL.connect(host='localhots', port=3306,
                       user=argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FORM 'state'")
    row = cur.fetchall()
    for states in row:
        print(states)
    cur.close()
    db.close()
