#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import urlopen
from pprint import pprint
if __name__ == "__main__":
  with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read().decode('utf-8')
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body))
