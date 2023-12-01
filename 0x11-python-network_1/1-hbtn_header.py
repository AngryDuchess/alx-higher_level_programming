#!/usr/bin/python3
"""
displays the value of the 'X-Request-Id' header
"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
