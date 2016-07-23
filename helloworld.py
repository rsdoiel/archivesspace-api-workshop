#!/usr/bin/env python3
import urllib.request
import json
import getpass

# This is where we add our functions
def hello_world():
    return 'Hello World!!!'

# This is where we add our tests
if __name__ == '__main__':
    hw = hello_world()
    if hw == 'Hello World!!!':
        print('Success!! ', hw)
    else:
        print('Ooops something went wrong, should say "Hello World!!!"')

