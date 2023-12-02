#!/usr/bin/python3
"""
post an email
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    req = requests.post(url, email)
    print(req.text)
