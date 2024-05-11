#!/bin/bash
# Send a HEAD request to the URL passed as an argument and capture the status code
curl -s -o /dev/null -w "%{http_code}\n" "$1"
