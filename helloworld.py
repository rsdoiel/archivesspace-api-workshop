#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error
import json

# This is where we add our functions
def hello_world(name, secret):
    print(name, 'has a secret...', secret)
    return 'Hello World!!!'

# This is where we add our tests
if __name__ == '__main__':
    import getpass
    name = input('Who are you? ')
    secret = getpass.getpass('Tell me a secret I can disclose...')
    hw = hello_world(name, secret)
    if hw == 'Hello World!!!':
        print('Success!! ', hw)
    else:
        print('Ooops something went wrong, should say "Hello World!!!"')

