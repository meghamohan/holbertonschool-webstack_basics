#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve a challenge
"""
import requests
import sys


if __name__ == '__main__':
    ownr = sys.argv[1]
    repoName = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(ownr, repoName)
    req = requests.get(url)
    res = req.json()
    if len(res) < 10:
        c = len(res)
    else:
        c = 10
    for i in res[:c]:
        print("{}: {}".format(i.get('sha'), i.get('commit').get('author').get('name')))
