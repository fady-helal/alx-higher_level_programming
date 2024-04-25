#!/usr/bin/python3

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and capture the HTTP status code and body
HTTP_RESPONSE=$(curl -s -w "\nHTTPSTATUS:%{http_code}\n" "$1")

# Extract the HTTP status code from the response
HTTP_STATUS=$(echo "$HTTP_RESPONSE" | tail -n 1 | cut -d' ' -f2)

# Check if the status code is 200
if [ "$HTTP_STATUS" -eq 200 ]; then
    # Display the body of the response
    echo "$HTTP_RESPONSE" | head -n -1
else
    echo "Request failed with status code: $HTTP_STATUS"
fi
