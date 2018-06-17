#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    req = requests.get(url)
    res = req.json()
    print("Number of result: {}".format(res['count']))
    c = 0
    for i in res['results']:
        c += 1
        print(i['name'])
    page = 2
    while c < res['count']:
        r = requests.get(url, params={'page': page}).json()
        page += 1
        for i in r['results']:
            c += 1
            print(i['name'])
