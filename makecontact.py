#!/usr/bin/env python3
import urllib.request

req = urllib.request.Request("http://localhost:8089")

with urllib.request.urlopen(req) as response:
    src = response.read().decode('UTF-8')
print(src)
