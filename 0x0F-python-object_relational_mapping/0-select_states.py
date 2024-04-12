#!/usr/bin/python3
"""Your comment"""
import sys
import mysql.connector
if __name__ == "__main__":
  conn = mysql.connector.connect(
  host = "localhost",
  port = 3306,
  user = sys.argv[1],
  password = sys.argv[2],
  database = sys.argv[3])
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM states ORDER BY id ASC")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  cursor.close()
  conn.close()

