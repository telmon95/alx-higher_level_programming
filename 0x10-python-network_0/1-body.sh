#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and display the body of the response
curl -s -o /tmp/body_response.txt -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" = "200" ]; then
        cat /tmp/body_response.txt
    fi
    rm /tmp/body_response.txt
}

