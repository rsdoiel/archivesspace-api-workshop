#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API returning an acccess token'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('utf-8')
    req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('utf-8')
    result = json.JSONDecoder().decode(src)
    auth_token = result['session']
    return auth_token

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    print('Logging in', api_url)
    s = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    print(s)
    print('Success!')
