#!/usr/bin/python3
"""
    Takes in a name of state and list
    all cities of state
"""


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

    query = """SELECT cities.name
                FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC"""

    cur = db.cursor()
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()
# Initialise empty list
    city_names = []
# Iterate
    for row in rows:
        # Add city names to list
        city_names.append(row[0])
# Join city names with commas
    print(", ".join(city_names))
