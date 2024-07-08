#!/usr/bin/python3
""" This module:
- Takes in a URL as a command-line argument.
- Sends a POST request to the passed URL with an email as a parameter.
- Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from command-line arguments.
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter and prepare the POST request.
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)

    # Send the request and print the response.
    with urllib.request.urlopen(request) as response:
        # Read the response body and decode it as UTF-8.
        response_body = response.read().decode("utf-8")
        print(response_body)
