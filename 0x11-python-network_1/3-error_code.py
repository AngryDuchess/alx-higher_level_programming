#!/usr/bin/python3
"""
get error code
"""
from urllib import request, error
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
