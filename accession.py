#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json
# Local modules
import login

def create_accession(api_url, auth_token, repo_id, accession_model):
    '''create an accession returning a status object'''
    data = json.JSONEncoder().encode(accession_model).encode('utf-8')
    url = api_url+'/repositories/'+str(repo_id)+'/accessions'
    req = urllib.request.Request(
             url = url,
             data = None,
             headers = {'X-ArchivesSpace-Session': auth_token},
             method = 'POST')
    try:
        response = urllib.request.urlopen(req, data)
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)


def list_accessions(api_url, auth_token, repo_id):
    '''List all the accessions for a given repo_id'''
    data = urllib.parse.urlencode({'all_ids': True}).encode('utf-8')
    url = api_url+'/repositories/'+str(repo_id)+'/accessions'
    req = urllib.request.Request(
        url = url,
        data = data,
        headers = {'X-ArchivesSpace-Session': auth_token},
        method = 'GET')
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)


def list_accession(api_url, auth_token, repo_id, accession_id):
    '''List an accession by repo_id and accession_id'''
    url = api_url+'/repositories/'+str(repo_id)+'/accessions/'+str(accession_id)
    req = urllib.request.Request(
         url = url,
         data = None,
         headers = {'X-ArchivesSpace-Session': auth_token},
         method = 'GET')
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)


def update_accession(api_url, auth_token, repo_id, accession_id, accession_model):
    '''update an accession record and return a results message'''
    data = json.JSONEncoder().encode(accession_model).encode('utf-8')
    url = api_url+'/repositories/'+str(repo_id)+'/accessions/'+str(accession_id)
    req = urllib.request.Request(
         url = url,
         data = None,
         headers = {'X-ArchivesSpace-Session': auth_token},
         method = 'POST')
    try:
        response = urllib.request.urlopen(req, data)
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)


def delete_accession(api_url, auth_token, repo_id, accession_id):
    '''delete an accession record and return a results message'''
    url = api_url+'/repositories/'+str(repo_id)+'/accessions/'+str(accession_id)
    req = urllib.request.Request(
         url = url,
         data = None,
         headers = {'X-ArchivesSpace-Session': auth_token},
         method = 'DELETE')
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        return None
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
    src = response.read().decode('utf-8')
    return json.JSONDecoder().decode(src)

if __name__ == "__main__":
    import getpass
    import datetime
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpace password: ')
    auth_token = login.login(api_url, username, password)

    # Test create_acccession
    print("Test create_accession()")
    repo_id = int(input('What is the repository id (numeric): '))

    print('Please provide the accession fields request')
    title = input('title: ')

    # This is the minimal Accession record
    accession_model = {
        'title': title,
        'id_0': 'test_'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'accession_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    result = create_accession(api_url, auth_token, repo_id, accession_model)
    print('Create accession result', json.dumps(result, indent=4))

    # Test list_accessions
    print('Test list_accessions()')
    accession_ids = list_accessions(api_url, auth_token, repo_id)
    print('Accession IDS', json.dumps(accession_ids, indent=4))

    # Test list_accession
    print('Test list_accession()')
    accession_id = int(input('Enter a numeric accession id: '))
    accession_model = list_accession(api_url, auth_token, repo_id, accession_id)
    print('Accession model', json.dumps(accession_model, indent=4))

    # Test update_accession
    print('Test update_accession()')
    accession_id = int(input('Enter accession id to update: '))
    accession_model = list_accession(api_url, auth_token, repo_id, accession_id)
    accession_model['title'] = input('Enter new title: ')
    result = update_accession(api_url, auth_token, repo_id, accession_id, accession_model)
    print('update result', json.dumps(result, indent=4))

    # Test delete_accession
    print('Test delete_accession()')
    accession_id = int(input('Enter accession id to delete: '))
    result = delete_accession(api_url, auth_token, repo_id, accession_id)
    print('delete result', json.dumps(result, indent=4))

    # All Done!
    print('Success!')

