#!/usr/bin/python3
"""
script take URL then send request and display
value of X-Request-Id var found in header
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
