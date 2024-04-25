#!/usr/bin/python3

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and display the size of the response body in bytes
curl -s -w "%{size_download}\n" "$1"
