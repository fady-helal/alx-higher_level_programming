#!/usr/bin/python3
import mysql.connector
import sys
if __name__ == "__main__":
  conn = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = sys.argv[1],
    password = sys.argv[2],
    database = sys.argv[3]
  )
  cursor = conn.cursor()
  cursor.execute("""SELECT cities.id, cities.name FROM
                  cities INNER JOIN states ON states.id=cities.states_id""")
rows = cursor.fetchall()
for row in rows:
  print(row)
cursor.close()
conn.close()
