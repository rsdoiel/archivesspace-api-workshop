import getpass
import urllib.request
    
def login ():
    username = input("ArchivesSpace username: ")
    password = getpass.getpass("ArchivesSpace pasword: ")
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request("http://localhost:8089/user/"+username+"/login", data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
        print(src)

login()
