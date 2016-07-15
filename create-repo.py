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
    authtoken = result['session']
    return auththoken

def create_repo(api_url, access_token, name, repo_code, org_code = "", image_url = "", url = ""):
    '''This function sends a create request to the ArchivesSpace REST API'''
    data = urllib.parse.urlencode({'jsonmodel_type': 'repository',
               'name': name,
               'repo_code': repo_code,
               'org_code': org_code,
               'image_url': image_url,
               'url': url})
    req = urllib.request.Request(api_url+'/repositories', 
               data, 
               {'X-ArchivesSpace-Session': access_token})
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
    return json.JSONDecoder().decode(src)

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    access_token = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
    repo = create_repo(api_url, access_token, input('Name: '), input('Repo Code: '), input('Org Code: '), input('Image URL: '),input('URL: '))
    print(json.dumps(repo, sort_keys: False, indent: 4))

