#!/usr/bin/python3
"""
send a post request and display a formatted json output
"""
import sys
import requests


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post(url, data={"q": letter})

    try:
        json_str = req.json()
        if ('id' in json_str and 'name' in json_str):
            print("[{}] {}".format(json_str.get('id'), json_str.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
