#!/usr/bin/python3
"""
fetch url using request library
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    txt = req.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
