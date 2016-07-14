#!/usr/bin/env python3
import urllib.request
import getpass
    
def login (username = "", password = ""):
    if username == "":
        username = input("ArchivesSpace username: ")
    if password == "":
        password = getpass.getpass("ArchivesSpace pasword: ")
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request("http://localhost:8089/user/"+username+"/login", data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
        print(src)

login()
