#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API returning an acccess token'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('utf-8')
    req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
    response = urllib.request.urlopen(req)
    result = json.JSONDecoder().decode(response.read().decode('utf-8'))
    # Session holds the value we want for auth_token
    return result['session']

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    print('Logging in', api_url)
    auth_token = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    print(auth_token)
    print('Success!')
