#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$1"
    fi
}

