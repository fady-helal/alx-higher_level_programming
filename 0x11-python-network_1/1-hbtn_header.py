#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header of the response"""
import sys
import urllib.request


if __name__ == "__main__":
  url = sys.argv[1]
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as response:
    body = response.read()
    headers = response.headers
    request_id = headers.get('X-Request-Id')
    if request_id:
      print(request_id)
