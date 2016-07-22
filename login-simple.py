#!/usr/bin/env python3
import urllib.request
import getpass
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API and shows the text response'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
    response = urllib.request.urlopen(req)
    return response.read().decode('UTF-8')

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    print('Logging in', api_url)
    s = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    print(s)
    print('Success!')
