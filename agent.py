#!/usr/bin/env python3
import urllib.request
import getpass
import json
from repo import *

def agent_type_url(api_url, agent_type):
   '''Map the agent type to a partial path'''
   # agent_person agent_corporate_entity agent_software agent_family user
   m = {
      'agent_person': 'people',
      'agent_corporate_entity': 'corporate_entities',
      'agent_software': 'software',
      'agent_family': 'families',
      'user': 'user'
   }
   return api_url+'/agents/'+m[agent_type]
 
def create_agent(api_url, auth_token, agent_record):
   '''create an agent and return the new agent record'''
   data = json.JSONEncoder().encode(agent_record).encode('utf-8')
   print("DEBUG data as json", data)
   req = urllib.request.Request(
        url = agent_type_url(api_url, agent_record['agent_type']),
        headers = {'X-ArchivesSpace-Session': auth_token},
        data = data,
        method = 'POST')
   response = urllib.request.urlopen(req)
   status = response.getcode()
   src = response.read().decode('utf-8')
   print("DEBUG status", status)
   print("DEBUG response", src)
   return json.JSONDecoder().decode(src)

if __name__ == '__main__':
    api_url = input('ArchivesSpace API URL: ')
    username = input('ArchivesSpace username: ')
    password = getpass.getpass('ArchivesSpace password: ')
    auth_token = login(api_url, username, password)
    agent_record = {
        'title': 'Ada Lovelace',
        'is_link_to_be_published': False,
        'agent_type': 'agent_person',
        'publish': False
    }
    print('agent_type_url()', agent_type_url(api_url, 'agent_person'))
    agent = create_agent(api_url, auth_token, agent_record)
    print("agent created", json.JSONEncoder().encode(agent))
