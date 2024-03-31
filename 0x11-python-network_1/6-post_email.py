#!/usr/bin/python3
"""
script takes URL and email address
Sends POST request to given URL with given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays body of response.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
