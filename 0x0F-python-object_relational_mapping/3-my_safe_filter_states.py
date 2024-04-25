#!/usr/bin/python3
"""your comment."""
import sys
import mysql.connector
if __name__ == "__main__":
  conn = mysql.connector.connect(
  host = "localhost",
  port = 3306,
  user = sys.argv[1],
  password = sys.argv[2],
  database = sys.argv[3]
  )
  name_search = sys.argv[4]
  cursor = conn.cursor()
  sql =  "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
  cursor.execute(sql, (name_search,))
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  cursor.close()
  conn.close()
