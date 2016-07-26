#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json
# Here's our own login module
import login


def create_repo(api_url, auth_token, name, repo_code, org_code = '', image_url = '', url = ''):
    '''create a repostory and return a status message'''
    data = json.JSONEncoder().encode({
                    'jsonmodel_type': 'repository',
                    'name': name,
                    'repo_code': repo_code,
                    'org_code': org_code,
                    'image_url': image_url,
                    'url': url
                }).encode('utf-8')
    req = urllib.request.Request(
            url = api_url+'/repositories', 
            data = None, 
            headers = {'X-ArchivesSpace-Session': auth_token})
    try:
        response = urllib.request.urlopen(req, data)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return ""
    except URLError as e:
        print(e.reason())
        return ""
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def list_repos(api_url, auth_token):
    '''List all the repositories'''
    req = urllib.request.Request(
        url = api_url+'/repositories',
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token})
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    except URLError as e:
        print(e.reason())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def list_repo(api_url, auth_token, repo_id):
    '''List a repository record'''
    req = urllib.request.Request(
        url = api_url+'/repositories/'+str(repo_id),
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token})
    try:
        response =  urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    except URLError as e:
        print(e.reason)
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def update_repo(api_url, auth_token, repo_id, repo):
    '''update a repository's metadata returning a status'''
    data = json.JSONEncoder().encode(repo).encode('utf-8')
    req = urllib.request.Request(
        url = api_url+'/repositories/'+str(repo_id),
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token})
    try:
        response = urllib.request.urlopen(req, data)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    except URLError as e:
        print(e.reason())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

def delete_repo(api_url, auth_token, repo_id):
    '''delete a repository returning a status'''
    req = urllib.request.Request(
        url = api_url+'/repositories/'+str(repo_id),
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token},
        method = 'DELETE')
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    except URLError as e:
        print(e.reason())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)


if __name__ == '__main__':
    import getpass
    # Test login
    print("Testing login()")
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpace password: ')
    print('Logging in', api_url)
    auth_token = login.login(api_url, username, password)
    print("auth token", auth_token)
    if auth_token != '':
        print('Success!')
    else:
        print('Ooops! something went wrong')
        sys.exit(1)

    # Test create_repo
    print('Testing create_repo()')
    print('Create your first repository')
    name = input('Repo name: ')
    repo_code = input('Repo code: ')
    repo = create_repo(api_url, auth_token, name, repo_code)
    print(json.dumps(repo, indent=4))
    print('Create a second repository')
    name = input('Repo name: ')
    repo_code = input('Repo code: ')
    repo = create_repo(api_url, auth_token, name, repo_code)
    print(json.dumps(repo, indent=4))

    # Test list_repos
    print('Testing list_repos()')
    repos = list_repos(api_url, auth_token)
    print('repositores list', json.dumps(repos, indent=4))

    # Test list_repo
    print('Testing list_repo()')
    repo_id = int(input('Enter repo id: '))
    repo = list_repo(api_url, auth_token, repo_id)
    print('repository list', json.dumps(repo, indent=4))
    
    # Test update_repo
    print('Testing update_repo()')
    repo_id = int(input('Repository numeric id to update: '))
    print('Getting repository record', repo_id)
    repo = list_repo(api_url, auth_token, repo_id)
    repo['name'] = input('old name is '+repo['name']+', provide a new name: ')
    print('Now we update')
    result = update_repo(api_url, auth_token, repo_id, repo)
    print('Result is', json.dumps(result, indent=4))
    
    # Test delete_repo
    print('Testing delete_repo()')
    repo_id = int(input('Repository numeric id to delete: '))
    result = delete_repo(api_url, auth_token, repo_id)
    print('Result is', json.dumps(result, indent=4))
    
    # All done!
    print('Success!')
