#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json
import getpass
# Local modules
import login

def create_accession(api_url, auth_token, repo_id, accession_model):
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


if __name__ == "__main__":
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
        'title': title
    }
    result = create_accession(api_url, auth_token, repo_id, accession_model)
    print('Create accession result', json.dumps(result, indent=4))

