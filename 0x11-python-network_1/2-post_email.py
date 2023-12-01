#!/usr/bin/python3
"""
sends a POST request with an email parameter
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf8'))
