#!/usr/bin/python3
from requests import post
import sys


"""
takes in a URL and an email address, sends
 a POST request to the passed URL with the email
 as a parameter, and finally displays the body of the response.
"""
if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    req = post(url=url, data={"email":mail})
    print(req.text)
