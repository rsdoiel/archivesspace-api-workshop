#!/usr/bin/env python3
import urllib
import json
import getpass
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API and shows the text response'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('utf-8')
    req = urllib.request.Request(
        url = api_url+'/users/'+username+'/login', 
        data = data)
    response = urllib.request.urlopen(req)
    status = response.getcode()
    print('HTTP status code', status)
    return response.read().decode('UTF-8')

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpacew password: ')
    print('Logging in', api_url)
    s = login(api_url, username, password)
    print(s)
    print('Success!')
