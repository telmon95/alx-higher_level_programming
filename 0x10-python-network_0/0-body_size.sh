#!/bin/bash

# Check if the script is provided with a URL argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL using curl and retrieve the body size
body_size=$(curl -sI "$1" | grep -i 'content-length' | awk '{print $2}')

# Display the body size in bytes
echo "$body_size"

