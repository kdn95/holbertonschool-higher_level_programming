#!/usr/bin/python3
"""List all states that start with the uppercase letter N"""


if __name__ == "__main__":
    import MySQLdb
    import sys

# Establish connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    state_name = """SELECT *
                    FROM states
                    WHERE BINARY `name` = '{0}'
                    ORDER BY id ASC
                    LIMIT 1""".format(sys.argv[4])
# Create cursor object to interact with db by executing SQL queries
    cur = db.cursor()
    cur.execute(state_name)
# fetchall() retrieves all rows returned from SQL query in execute()
    rows = cur.fetchall()
# Returns list of tuples. Each tuple is a row from the result set of the query
    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))
