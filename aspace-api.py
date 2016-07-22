#!/usr/bin/env python3
import urllib.request
import os
import sys
import json


class ArchivesSpaceAPI:
    '''ArchiveSpaceAPI provides an object for interacting with the ArchivesSpace REST API'''
    Version = '0.0.0'
    def __init__(self):
        self.jsonparse = json.JSONDecoder().decode
        self.username = os.environ.get('ASPACE_USERNAME')
        self.password = os.environ.get('ASPACE_PASSWORD')
        self.auth_token = ''
        self.api_url = os.environ.get('ASPACE_API_URL')
        problem = False
        errors = []
        if not self.username:
            errors.append('Missing ASPACE_USERNAME in environment')
        if not self.password:
            errors.append('Missing ASPACE_PASSWORD in environment')
        if not self.api_url:
            errors.append('Missing ASPACE_API_URL in environment')
        if len(errors) > 0:
            raise Exception(', '.join(errors))

    def login(self):
        '''Based on the current system environment log into the ArchivesSpace REST API'''
        data = urllib.parse.urlencode({'password': self.password})
        data = data.encode('ascii')
        req = urllib.request.Request(self.api_url+'/users/'+self.username+'/login', data)
        response = urllib.request.urlopen(req)
        result = self.jsonparse(response.read().decode('UTF-8'))
        self.auth_token = result['session']
        return result


    def createRepository(self, repo_code, name):
        '''Create a repository, return the created object'''
        data = urllib.parse.urlencode({
            'repo_code': repo_code,
            'name': name,
        }).encode('ascii')
        req = urllib.request.Request(self.api_url+'/repositories', None, {'X-ArchivesSpace-Session': self.auth_token})
        response =  urllib.request.urlopen(req, data)
        return json.JSONDecoder().decode(response.read().decode('UTF-8'))


    def listRepositories(self):
        req = urllib.request.Request(self.api_url+'/repositories', None, {'X-ArchivesSpace-Session': self.auth_token})
        response = urllib.request.urlopen(req)
        return self.jsonparse(response.read().decode('UTF-8'))

    def getRepository(self, repo_id):
        raise Exception('getRepository(%s)' % repo_id)

    def removeRepository(self, repo_id):
        raise Exception('removeRepository(%s)' % repo_id)

#
# Testing of ArchivesSpaceAPI
#
class Flags:
    flags = {}
    index = {}
    docs = []
    args = []
    parsed = {}

    def get(self, flag):
        key = flag.lstrip('-').strip()
        if flag in self.index:
            key = self.index[flag]
        if key in self.flags:
            return self.flags[key]
        return False


    def set(self, shortflag, longflag, default, msg):
        self.index[shortflag.strip()] = longflag.strip()
        self.flags[longflag.strip()] = default
        self.docs.append('-'+shortflag+', --'+longflag+'    '+msg)

    def printDefaults(self):
        for v in self.docs:
            print(v)

    def parse(self, args):
        for i in range(len(args)):
            arg = args[i]
            if '-' == arg[0:1]:
                key = arg.lstrip('-').strip()
                if key in self.index:
                    key = self.index[key]
                if key in self.flags:
                    val = self.flags[key]
                    if '=' in key:
                        (key, val) = key.split('=', 2)
                    elif (i+1) < len(args) and args[i+1][0:1] != '-':
                        val = args[i+1]
                    else:
                        val = True
                    self.flags[key] = val




def main():
    '''Test ArchivesSpaceAPI Class'''
    flags = Flags()
    flags.set('h', 'help', False, 'display help information')
    flags.set('v', 'version', False, 'display version information')
    flags.set('r', 'read', False, 'run read api tests')
    flags.set('w', 'write', False, 'run write/update tests')

    flags.parse(sys.argv)

    print('Checking for problems in environment...')
    try:
        api = ArchivesSpaceAPI()
    except Exception as err:
        print('Unexpected error:', err)
        sys.exit(1)

    if flags.get('help'):
        print('USAGE %s [OPTIONS]' % sys.argv[0])
        flags.printDefaults()
        print('Version %s' % api.Version)
        sys.exit(0)

    if flags.get('version'):
        print('Version %s' % api.Version)
        sys.exit(0)

    print('Logging into API')
    try:
        result = api.login()
    except Exception as err:
        print(err)
        sys.exit(1)
    if api.auth_token != result['session']:
        print("Expecting api.auth_token == result.sessions: ", api.auth_token, result['session'])
    else:
        print('Login test OK')

    if flags.get('read'):
        print('Running read API tests...')
        try:
            result = api.listRepositories()
        except Exception as err:
            print(err)
            sys.exit(1)
        print('Repository list', result)
        # FIXME: loop through results and make sure I can get individual repository details
    else:
        print('Skipping read API tests...')

    if flags.get('write'):
        print('Running write API tests...')
        try:
            result = api.createRepository('API Test', 'test0')
        except Exception as err:
            print(err)
            sys.exit(1)
        print(result)
        # FIXME: With result, append ' updated' to result.name and verify the update was successful
        # FIXME: With result, remove the created repository to confirm final write accession works
    else:
        print('Skipping write API tests...')


if __name__ == '__main__':
    main()
