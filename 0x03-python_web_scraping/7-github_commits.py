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
    for i in res[:10]:
        print(i.get('sha') + ': ' + i.get('commit').get('author').get('name'))
