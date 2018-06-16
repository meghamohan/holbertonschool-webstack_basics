#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    req = requests.get(url)
    res = req.json()
    print("Number of result: {}".format(res['count']))
    for i in range(0, res['count']):
        try:
            print(res['results'][i]['name'])
        except Exception:
            break
