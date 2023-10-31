#!/usr/bin/env python3
import requests
import sys


if len(sys.argv) < 2:
    print("Please input the preferred language")
    sys.exit(1)

language = sys.argv[1]
url = "http://localhost:5000/"
headers = {"Accept-Language": "{}".format(language)}  # Set the preferred language to French

response = requests.get(url, headers=headers)

print(response.text)

