#!/usr/bin/python3
"""
makes request to github's api and displays user id
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = f'https://api.github.com/user/{user}'

    req = requests.get(url, auth=HTTPBasicAuth(user, pwd))
    print(req.json().get('id'))
