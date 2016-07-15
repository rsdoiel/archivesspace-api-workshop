#!/usr/bin/env python3
import urllib.request

api_url = input('ArchivesSpace API URL: ')
if api_url == '':
    api_url = 'http://localhost:8089'
req = urllib.request.Request(api_url)

with urllib.request.urlopen(req) as response:
    src = response.read().decode('UTF-8')
print(src)
