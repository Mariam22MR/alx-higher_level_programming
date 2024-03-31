#!/usr/bin/python3
"""
script take URL and email, Sends POST request to given URL with given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    email = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], email)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
