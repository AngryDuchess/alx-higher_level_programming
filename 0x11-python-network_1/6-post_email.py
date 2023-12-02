#!/usr/bin/python3
"""
post an email
"""
import requests
import sys


if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[2]}

    req = requests.post(url, email)
    print(req.text)
