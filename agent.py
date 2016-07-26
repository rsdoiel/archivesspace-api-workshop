#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json
# Import our own login module
import login

def agent_type_path(agent_type):
   '''Map the agent type to a partial path'''
   # agent_person agent_corporate_entity agent_software agent_family user
   m = {
      'agent_person': 'people',
      'agent_corporate_entity': 'corporate_entities',
      'agent_software': 'software',
      'agent_family': 'families',
      'user': 'user'
   }
   return '/agents/'+m[agent_type]

def create_agent(api_url, auth_token, agent_model):
   '''create an agent and return the new agent record'''
   data = json.JSONEncoder().encode(agent_model).encode('utf-8')
   url = api_url+agent_type_path(agent_model['agent_type'])
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


def list_agents(api_url, auth_token, agent_type):
   '''List all the agent ids of a given type'''
   data = urllib.parse.urlencode({'all_ids': True}).encode('utf-8')
   url = api_url+agent_type_path(agent_type)
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
   

def list_agent(api_url, auth_token, agent_type, agent_id):
   '''List an agent by agent_type and agent_id'''
   url = api_url+agent_type_path(agent_type)+'/'+str(agent_id)
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


def update_agent(api_url, auth_token, agent_type, agent_id, agent_model):
   '''update an agent record returning a status'''
   data = json.JSONEncoder().encode(agent_model).encode('utf-8')
   url = api_url+agent_type_path(agent_type)+'/'+str(agent_id)
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


def delete_agent(api_url, auth_token, agent_type, agent_id):
   '''delete an agent by agent_type and agent_id'''
   url = api_url+agent_type_path(agent_type)+'/'+str(agent_id)
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
   
if __name__ == '__main__':
    import getpass
    # Get enough info to reach the API
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = input('ArchivesSpace password: ') #getpass.getpass('ArchivesSpace password: ')

    # Get our auth token by logging in
    auth_token = login.login(api_url, username, password)

    # check mapping of agent type (e.g. agent_person) to path
    print('Check that our mapping of agent type to path works')
    url_test = agent_type_path('agent_person')
    if url_test != '/agents/people':
       print('ERROR: expected .../agents/people, found ', url_test)
       sys.exit(0)
    else:
       print('agent_type_path() OK')

    # Test create_agent()
    print('Testing create_agent')
    # Here's our minimal fields
    primary_name = input('Primary name (e.g. family name) ')
    rest_of_name = input('Rest of name (e.g. first name) ')
    agent_type = 'agent_person'
    source = 'local'
    rules = 'local'

    # Our minimal agent record includes a :name_person and a :agent_person
    # model
    name_model = {
           'primary_name': primary_name,
           'rest_of_name': rest_of_name,
           'name_order': 'inverted',
           'jsonmodel_type': 'name_person',
           'source': source,
           'rules': rules,
           'sort_name': primary_name+', '+rest_of_name,
           'is_display_name': True,
    }

    agent_model = {
        'jsonmodel_type': agent_type,
        'title': primary_name+', '+rest_of_name,
        'is_link_to_be_published': False,
        'agent_type': agent_type,
        'publish': False,
        'display_name': name_model,
        'names':[
           name_model
         ]
    }

    # Now that we have a minimal record lets make a request
    print("The minimum payload looks like ", json.dumps(agent_model, indent=4))
    agent_response = create_agent(api_url, auth_token, agent_model)
    agent_id = agent_response['id']
    print('agent created response', json.dumps(agent_response, indent=4))


    # Test list_agents(), requires api_url, auth_token and agent_type
    print('Test list_agents()')
    agent_ids = list_agents(api_url, auth_token, 'agent_person')
    if len(agent_ids) < 1:
       print('ERROR: should have at least one agent!')
       sys.exit(0)
    print('agent ids ->', json.dumps(agent_ids, indent = 4))

    # Test list_agent(), requires api_url, auth_token, agent_type, agent_id
    print('Test list_agent()')
    agent_id = input('Enter agent_id (numeric): ')
    agent = list_agent(api_url, auth_token, 'agent_person', agent_id)
    print('agent', agent_id, ' details', json.dumps(agent, indent=4))


    # Test update_agent
    agent_type = 'agent_person'
    agent_id = int(input('Enter agent id to update: '))
    note_text = input('Enter some text to add as a note: ')
    agent_model = list_agent(api_url, auth_token, agent_type, str(agent_id))

    note_count = len(agent_model['notes'])
    if (note_count > 0):
        print('The existing notes are', json.dumps(agent_model['notes'], indent=4))

    new_note = {
        'jsonmodel_type': 'note_bioghist',
        'persistent_id': 'urn:test.a.note.to.self/'+str(note_count+1),
        'label': 'Personal note to self',
        'subnotes': [
            {
                'jsonmodel_type': 'note_text',
                'content': note_text,
                'publish': True
            }
        ],
        'publish':True
    }
    # now adding a new note
    agent_model['notes'].append(new_note)
    print("Added a note", json.dumps(agent_model['notes'], indent=4))
    res = update_agent(api_url, auth_token, agent_type, 3, agent_model)
    print('Response was', json.dumps(res, indent=4))


    # Test delete_agent()
    print('Testing delete_repo()')
    agent_id = int(input('Agent numeric id to delete: '))
    result = delete_agent(api_url, auth_token, agent_type, agent_id)
    print('Result is', json.dumps(result, indent=4))

    # All done!
    print('Success!')
