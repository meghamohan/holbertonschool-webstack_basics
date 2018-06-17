#!/usr/bin/python3
"""

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
        count = len(res)
    else:
        count = 10
    for i in range(0, count):
        print(res[i]['sha'] + ': ' + res[i]['commit']['author']['name'])
        count -= 1
