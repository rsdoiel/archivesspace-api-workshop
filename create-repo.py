#!/usr/bin/env python3
import urllib.request
import getpass
import json
    
def login (api_url, username, password):
    '''This function takes a username/password and authenticates against the ArchivesSpace REST API'''
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
    response = urllib.request.urlopen(req)
    result = json.JSONDecoder().decode(response.read().decode('UTF-8'))
    # Session in the property that holds our auth_token value.
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
    return json.JSONDecoder().decode(response.read().decode('utf-8'))

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpace password: ')
    name = input('Repo name: ')
    repo_code = input('Repo code: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    auth_token = login(api_url, username, password)
    print('username', username, 'auth_token', auth_token)
    repo = create_repo(api_url, auth_token, name, repo_code)
    print(json.dumps(repo, indent=4))
