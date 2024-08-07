#!/usr/bin/python3
"""
Module that fetches https://alx-intranet.hbtn.io/status
- use the package urllib
- not allowed to import any packages other than urllib
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
