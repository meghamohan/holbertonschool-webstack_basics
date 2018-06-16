#!/usr/bin/python3
"""
takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    user = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/users/'
    req = requests.get(url, auth=HTTPBasicAuth(user, pswd))
    res = req.json()
    print(res)
    try:
        print(res['id'])
    except:
        print("None")
