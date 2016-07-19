#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (api_url, username, password):
    '''This function takes a username/password and authenticates against the ArchivesSpace REST API'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
    result = json.JSONDecoder().decode(src)
    return result['session']

def create_repo(api_url, auth_token, name, repo_code, org_code = "", image_url = "", url = ""):
    '''This function sends a create request to the ArchivesSpace REST API'''
    # Data is getting attached to urlopen() and not req object to trigger a POST
    # ArchivesSpace API likes JSON encoding rather than URL encoding like login
    data = json.JSONEncoder().encode({
                    'jsonmodel_type': 'repository',
                    'name': name,
                    'repo_code': repo_code,
                    'org_code': org_code,
                    'image_url': image_url,
                    'url': url
                }).encode('utf-8')
    # Add our auth_token to your req object
    req = urllib.request.Request(api_url+'/repositories', None, {'X-ArchivesSpace-Session': auth_token})
    response = urllib.request.urlopen(req, data)
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def list_repos(api_url, auth_token):
    '''List all the repositories, return the listing object'''
    req = urllib.request.Request(
        api_url+'/repositories',
        None,
        {'X-ArchivesSpace-Session': auth_token})
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def list_repo(api_url, auth_token, repo_id = 0):
    '''List all the repositories, return the listing object'''
    req = urllib.request.Request(
        api_url+'/repositories/'+repo_id,
        None,
        {'X-ArchivesSpace-Session': auth_token})
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpace password: ')
    auth_token = login(api_url, username, password)
    print('username', username, 'auth_token', auth_token)
    repo_id = int(input('Enter repo id: '))
    repo = list_repo(api_url, auth_token, repo_id)
    print('repositores list', json.dumps(repos, indent=4))
    
