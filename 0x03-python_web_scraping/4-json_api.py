#!/usr/bin/python3
"""
takes in a letter and sends a POST request
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res = req.json()
    except:
        print("Not a valid JSON")
    if res:
        print("[{}] {}".format(res.get('id'), res.get('name')))
    else:
         print("No result")
