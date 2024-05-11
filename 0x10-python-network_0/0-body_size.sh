#!/bin/bash
# Command to display the size of the content in a header
curl -sI $1 | grep Content-Length | cut -d" " -f2
