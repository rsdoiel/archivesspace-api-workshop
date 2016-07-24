#!/usr/bin/env python3
import urllib.request
import getpass
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

def list_agents(api_url, auth_token, agent_type):
   '''List all the agent ids of a given type'''
   data = urllib.parse.urlencode({'all_ids': True}).encode('utf-8')
   url = api_url+agent_type_path(agent_type)
##   print('DEBUG: curl -H "{X-ArchivesSpace-Session:', auth_token, '}"',
##         url+'?all_ids=true') # DEBUG
   req = urllib.request.Request(
      url = url,
      data = data,
      headers = {'X-ArchivesSpace-Session': auth_token},
      method = 'GET')
   response = urllib.request.urlopen(req)
   status = response.getcode()
   if status != 200:
      print('WARNING: https status code ', status)
      return response.read().decode('utf-8')
   agent_ids = json.JSONDecoder().decode(response.read().decode('utf-8'))
   return agent_ids
   

def list_agent(api_url, auth_token, agent_type, agent_id):
   '''List all the agent ids of a given type'''
   url = api_url+agent_type_path(agent_type)+'/'+agent_id
##   print('DEBUG: curl -H "{X-ArchivesSpace-Session:', auth_token, '}"',
##         url) # DEBUG
   req = urllib.request.Request(
      url = url,
      data = None,
      headers = {'X-ArchivesSpace-Session': auth_token},
      method = 'GET')
   response = urllib.request.urlopen(req)
   status = response.getcode()
   if status != 200:
      print('WARNING: https status code ', status)
   agent = json.JSONDecoder().decode(response.read().decode('utf-8'))
   return agent
   
   
def create_agent(api_url, auth_token, agent_record):
   '''create an agent and return the new agent record'''
   data = json.JSONEncoder().encode(agent_record).encode('utf-8')
   url = api_url+agent_type_path(agent_record['agent_type'])
##   print('DEBUG curl -H {"X-ArchivesSpace-Session: ',
##         auth_token,
##         '"} ',
##         ' -d ',
##         data,
##         ' ',
##         url)
   req = urllib.request.Request(
        url = url,
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token},
        method = 'POST')
   response = urllib.request.urlopen(req, data)
   status = response.getcode()
   src = response.read().decode('utf-8')
   if status != 200:
      print('DEBUG response', src)
      return src
   return json.JSONDecoder().decode(src)

def update_agent(api_url, auth_token, agent_record):
   '''create an agent and return the new agent record'''
   data = json.JSONEncoder().encode(agent_record).encode('utf-8')
   url = api_url+agent_type_path(agent_record['agent_type'])
##   print('DEBUG curl -H {"X-ArchivesSpace-Session: ',
##         auth_token,
##         '"} ',
##         ' -d ',
##         data,
##         ' ',
##         url)
   req = urllib.request.Request(
        url = url,
        data = None,
        headers = {'X-ArchivesSpace-Session': auth_token},
        method = 'POST')
   response = urllib.request.urlopen(req, data)
   status = response.getcode()
   src = response.read().decode('utf-8')
   if status != 200:
      print('DEBUG response', src)
      return src
   return json.JSONDecoder().decode(src)

if __name__ == '__main__':
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

    agent_record = {
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
    print("The minimum payload looks like ", json.dumps(agent_record, indent=4))
    agent_response = create_agent(api_url, auth_token, agent_record)
    agent_id = agent_response['id']
    print('agent created response', json.dumps(agent_response, indent=4))

    # Update the record we just created
    agent_id = int(input('Enter agent id to update: '))
    agent_record = list_agent(api_url, auth_token, agent_type, str(agent_id))
    print('Updating ', agent_id)
    new_primary_name = input('Add a new primary name: ')
    new_rest_of_name = input('Add a new rest of name: ')
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
    agent_record['names'].append(name_model)
    agent_record['display_name'] = name_model
    # FIXME: Need to go through and adjust all the times and
    # person updating in each of the models...
    agent_response = update_agent(api_url, auth_token, agent_record)
    print('agent update response', json.dumps(agent_response, indent=4))
