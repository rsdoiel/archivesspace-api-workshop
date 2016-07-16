#!/usr/bin/env python3
import urllib.request
import json
import getpass

api_url = input('ArchivesSpace API URL: ')
if api_url == '':
    api_url = 'http://localhost:8089'
req = urllib.request.Request(api_url)

with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))

