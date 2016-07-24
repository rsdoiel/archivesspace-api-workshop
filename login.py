#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API returning an acccess token'''
    data = urllib.parse.urlencode({'password': password}).encode('utf-8')
    req = urllib.request.Request(
        url = api_url+'/users/'+username+'/login', 
        data = data)
    response = urllib.request.urlopen(req)
    status = response.getcode()
    if status != 200:
        # No session token
        print('ERROR: login failed', response.read().decode('utf-8'))
        return ''
    result = json.JSONDecoder().decode(response.read().decode('utf-8'))
    # Session holds the value we want for auth_token
    return result['session']

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpacew password: ')
    print('Logging in', api_url)
    auth_token = login(api_url, username, password)
    print(auth_token)
    if auth_token != '':
        print('Success!')
    else:
        print('Ooops! something went wrong')
