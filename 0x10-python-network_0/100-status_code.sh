#!/bin/bash

# Send a HEAD request to the URL passed as an argument and capture the status code
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}\n" "$1")

# Display the status code
echo $STATUS_CODE

