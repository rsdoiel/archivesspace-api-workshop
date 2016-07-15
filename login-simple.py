#!/usr/bin/env python3
import urllib.request
import getpass
    
def login (username, password):
    '''This function logs into the ArchivesSpace REST API and shows the text response'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request('http://localhost:8089/users/'+username+'/login', data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
    return src

if __name__ == '__main__':
    print('Logging in')
    s = login(input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    print(s)
    print('Success!')
