#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json
    
def login (api_url, username, password):
    '''This function logs into the ArchivesSpace REST API returning an acccess token'''
    data = urllib.parse.urlencode({'password': password}).encode('utf-8')
    req = urllib.request.Request(
        url = api_url+'/users/'+username+'/login', 
        data = data)
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return ""
    except URLError as e:
        print(e.reason())
        return ""
    src = response.read().decode('utf-8')
    result = json.JSONDecoder().decode(src)
    # Session holds the value we want for auth_token
    return result['session']

if __name__ == '__main__':
    import getpass
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
