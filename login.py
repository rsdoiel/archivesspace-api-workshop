#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (username, password):
    '''This function logs into the ArchivesSpace REST API returning an acccess token'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request('http://localhost:8089/users/'+username+'/login', data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
    result = json.JSONDecoder().decode(src)
    authtoken = result['session']
    return auththoken

if __name__ == '__main__':
    print('Logging in')
    s = login(input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    print(s)
    print('Success!')
