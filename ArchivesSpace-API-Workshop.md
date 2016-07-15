
# Introducing the ArchivesSpace REST API using Python 3

+ [R. S. Doiel](https://rsdoiel.github.io)
    + Software Developer 
    + Caltech Library
+ [Mark Custer](https://resources.library.yale.edu/StaffDirectory/detail.aspx?q=702)
    + Archivist and Metadata Coordinator
    + Beinecke Rare Book and Manuscript Library

[Presentation website](./)

[Download slides](./archivesspace-api-workshop-slides.zip)

--

## Requirements

Requirements for participants:

+ A laptop/device with network access
    + Linux (what I use), Mac OS X (which I am familiar with), or Windows (which I am very rusty on)
    + Python 3 installed including the python standard library (see https://docs.python.org/3/library/)
        + Python 3 (v3.5.2) can be downloaded and from https://www.python.org/downloads/
        + We’ll be making heavy use of http, json modules
+ A Text Editor (if they don’t have one I recommend Atom Editor at http://atom.io)
+ A web browser (recommend Firefox or Chrome with the JSONView plugin https://jsonview.com/)
+ Access to ArchivesSpace REST API (will be provided at conference)
    + If you have [Virtualbox]()/[Vagrant]() 
    + Use [archivesspace-dev](https://github.com/rsdoiel/archivesspace-api-workshop/archivesspace-dev) from the Workshop website

Recommended:

Read through https://docs.python.org/3/tutorial/index.html if they are not familiar with Python.
Bookmark in your web browser: http://archivesspace.github.io/archivesspace/api/
Bookmark in your web browser: https://docs.python.org/3/library/index.html

--

## Before the workshop

+ Make sure you have a modern web browser
    + I suggest either Firefox or Chrome
+ Install [Python 3.5.2](https://www.python.org/downloads/) if needed
+ Make sure you have [Python 3.5.2](https://www.python.org/downloads/) 
+ Make sure you have a text editor
    + Examples
        + [Atom](http://atom.io)
        + [Brackets](http://brackets.io)
        + vi, emacs, nano, pico, etc
    + Or the Python IDE that comes with Python
+ A test deployment ArchivesSpace is being provided as part of the Workshop
    + You can install your own [Vagrant](http://github.com/rsdoiel/archivesspace-api-workshop/archivesspace-dev/)

--

# Workshop Overview

+ What we'll be covering
    + ArchivesSpace REST API
    + Using Python 3 for interacting with the REST API
+ More generally
    + REST APIs as Data Sources
    + Working with JSON data
+ Identifying helpful web resources

--

# Workshop structure

1. Setup
2. Making an http connection
3. Authentication
4. Repositories
5. Working with Agents
6. Working with Accessions
7. Working with Digital Objects
8. Working in Batches

--

# 1. Setup

## your web browser

+ Bookmark the following
    + [rsdoiel.github.io/archivesspace-api-workshop](https://rsdoiel.github.io/archivesspace-api-workshop) - so you can follow along
    + ArchivesSpace API docs [archivesspace.github.io/archivesspace/api/](http://archivesspace.github.io/archivesspace/api/)
    + Python tutorial [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/index.html)
    + Python library reference [docs.python.org/3/library](https://docs.python.org/3/library/index.html)
+ Optional
    + [JSONView](https://jsonview.com/) browser plugin (e.g. Firefox, Chrome)
    + Stephen Dolan's [jq](https://stedolan.github.io/jq/) for the command line
    + [Curl](https://curl.haxx.se/) for debugging web connections

--

# 1. Setup 

## Python/your text editor

+ Make sure you have [Python 3.5.2](https://www.python.org/downloads/) available
    + try **python --version**
    + The website has easy installers for Windows and Mac OS X
+ Do you have a text editor?
    + You can use [Python 3's IDE](https://www.python.org/downloads/)
    + A text editor like [Atom](http://atom.io), [Brackets](http://brackets.io/), SubEthaEdit and Sublime
    + Or event console based editors like vi, emacs, nano, pico

--

# 1. Setup 

## ArchivesSpace

+ Our hosts have provided us with test deployments of ArchivesSpace
    + See hand out or whiteboard for connection details
+ If you want to work on your own
    + Under virtualbox/vagrant 
    + try [github.com/rsdoiel/archivesspace-api-workshop](https://github.com/rsdoiel/archivesspace-api-workshop)/archivesspace-dev
+ Make sure you can access ArchivesSpace from your web browser
    + On a stock install check the following ports
        + 8080 - ArchivesSpace Web UI (e.g. http://localhost:8080)
        + 8089 - ArchivesSpace REST API (e.g. http://localhost:8089)

--

# 2. Make an http connection

## Let's get started

At this point your setup should be completed and we're
going to start coding in Python 3.

--

# 2. Make an http connection

In three parts

+ launch the Python interpreter
+ import the http client module
+ make a connection with the request object

--

# 2. Make an http connection

## launch python

```shell
    python3
```

--

# 2. Make an http connection

## import the module

```python
    import urllib.request
```

--

# 2. Make an http connection

## Create a request object

```python
    api_url = 'http://localhost:8089'
    req = urllib.request.Request(api_url)
```

You will need to replace "http://localhost:8089" with your 
Workshop URL.

--

# 2. Make an http connection

## Make the request, print results

```python
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
        print(src)
```

Exit your python3 interpreter 

```python
    exit()
```

--

# 2. Make an http connection

## Putting it all together

Put this into a text file called [make-an-http-connection.py](make-an-http-connection.py)

```python
    #!/usr/bin/env python3
    import urllib.request

    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    req = urllib.request.Request(api_url)

    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
        print(src)
```

--

# 3. Authentication

## Basic ingredients

+ Make an http connection
+ Send our username and pasword
+ Save the access token returned

--

# 3. Authentication

## Send our username and password

### IMPORTANT!!!!

I am going show a BAD practice by hardcoding a 
username and password. This is just to make teaching 
easier. In real life you want to use a configuration 
file or environment variables (my preferred).

--

# 3. Authentication

## Send our username and password

We need pass our username and password in our request.
We need to keep track of the response. You don't need to
type of the python comments.

Launch our Python interpreter again.

```python
    import urllib.request

    api_url = 'http://localhost:8089'
    
    # Hardcoding a username/password is BAD PRACTICE!!!!
    username = "admin" # or what you named your account
    password = "admin" # or what you set the password to
```

--

# 3. Authentication

## Send our username and password

Encode our password for sending with our request.

```python
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
```

--

# 3. Authentication

# Send our username and password

Now with our data send our request.

```python
    req = urllib.request.Request(api_url+"/users/"+username+"/login", data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
        print(src)
```

Exit our python interpreter 

```python
    exit()
```

--

# 3. Authentication

## Send our username and password

### Putting it all together

Put this into a text file called **login-simple.py**. We'll
create a python function and prompt for api url, username 
and password.

```python
    #!/usr/bin/env python3
    import urllib.request
    import getpass
        
    def login (api_url, username, password):
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('ascii')
        req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        return src
    
    if __name__ == '__main__':
        api_url = input('ArchivesSpace API URL: ')
        if api_url == '':
            api_url = 'http://localhost:8089'
        print('Logging in')
        s = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
        print(s)
        print('Success!')
```

--

# 3. Authentication

## Notice the JSON about

Open [example-login-response.json](example-login-response.json) in a new browser window.

--

# 3. Authentication

## Save the access token returned

We need to parse the JSON data into a Python object
so we can save our access token.

```JSON
    {   
       "session": "84467334ce001b924b0e6d529edf99e383.5.271d4238177ab2e811dc5ac9e5a",
       ...
    }
```

The session value is our access token.

--

# 3. Authentication

## Save the access token returned

We just need to **import json** and modify our login
function to **parse the JSON response and return 
the session value**. Copy [login-simple.py](login-simple.py)
to [login.py](login.py) and make the changes.

```python
    #!/usr/bin/env python3
    import urllib.request
    import getpass
    import json
        
    def login (api_url, username, password):
        '''This function logs into the ArchivesSpace REST API returning an access token'''
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('ascii')
        req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        result = json.JSONDecoder().decode(src)
        return result['session']
    
    if __name__ == '__main__':
        api_url = input('ArchivesSpace API URL: ')
        if api_url == '':
            api_url = 'http://localhost:8089'
        print('Logging in')
        s = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
        print("Your access token was: ", s)
        print('Success!')
```

--

# 4. Repositories

+ Creating a two repositories 
    + we'll keep the first and experiment with the second
+ View the repository information
+ List the available repositories
+ Deleting the second repository

--

# 4. Repositories

Creating a repository requires

+ login to API with appropriate account (e.g. admin)
+ package a request to create a repository
+ send the request to create the repository saving the response

We repeat the process to create another one.
--

# 4. Repositories

## Creating our create_repo function

+ Go to [AS REST API docs](http://archivesspace.github.io/archivesspace/api/#get-repositories)
    + We're interested in "Create a Repository"
+  Look at the example **Curl** request on the right


```json
    curl -H "X-ArchivesSpace-Session: $SESSION"
    -d {
       "jsonmodel_type": "repository",
       "name": "Description: 11",
       "repo_code": "ASPACE REPO 2 -- 631024",
       "org_code": "970UV228G",
       "image_url": "http://www.example-3.com",
       "url": "http://www.example-4.com"
    } 
    'http://localhost:8089/repositories'
```

(the bit with "-d" is what we're interested in.)

--

# 4. Repositories

## Creating our create_repo function

The elements we're change with each request will form the parameters in our function.
They are two required elements and the rest are optional

### required

+ name
+ repo_code (a unique screen we'll decide on)

### optional

+ org_code 
+ image_url
+ url

### What we also need

+ We will need to submit our access token too

--

# 4. Repositories

## Reusing our login function

1. Copy [login.py](login.py) to [create-repo.py](create-repo.py)
2. Remove everything except import statements and login function
3. We're now read to add a new create_repo function

--

# 4. Repostories

Our function definition should look something like

```python
    def create_repo(api_url, access_token, name, repo_code, org_code = "", image_url = "", url = ""):
        '''This function sends a create request to the ArchivesSpace REST API'''
```

Did we catch all the fields we might want to change?

```json
    {
       "jsonmodel_type": "repository",
       "name": "Description: 11",
       "repo_code": "ASPACE REPO 2 -- 631024",
       "org_code": "970UV228G",
       "image_url": "http://www.example-3.com",
       "url": "http://www.example-4.com"
    } 
```

--

# 4. Repositories

Now lets flesh out a **create_repo** function.

```python
    def create_repo(api_url, access_token, name, repo_code, org_code = "", image_url = "", url = ""):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = urllib.parse.urlencode({'jsonmodel_type': 'repository',
               'name': name,
               'repo_code': repo_code,
               'org_code': org_code,
               'image_url': image_url,
               'url': url})
        req = urllib.request.Request(api_url+'/repositories', 
                data, 
                {'X-ArchivesSpace-Session': access_token})
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        return json.JSONDecoder().decode(src)
```

Notice how similar it is to our **login** function. Also how we
add the header to pass along with our request.

--

# 4. Repositories

Putting it all together

```python
    #!/usr/bin/env python3
    import urllib.request
    import getpass
    import json
    
    def login (api_url, username, password):
        '''This function takes a username/password and authenticates against the ArchivesSpace REST API'''
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('ascii')
        req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        result = json.JSONDecoder().decode(src)
        return result['session']

    def create_repo(api_url, access_token, name, repo_code, org_code = "", image_url = "", url = ""):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = urllib.parse.urlencode({'jsonmodel_type': 'repository',
               'name': name,
               'repo_code': repo_code,
               'org_code': org_code,
               'image_url': image_url,
               'url': url})
        req = urllib.request.Request(api_url+'/repositories', 
               data, 
               {'X-ArchivesSpace-Session': access_token})
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        return json.JSONDecoder().decode(src)

    if __name__ == '__main__':
        api_url = input('ArchivesSpace API URL: ')
        if api_url == '':
            api_url = 'http://localhost:8089'
        access_token = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
        repo = create_repo(api_url, access_token, input('Name: '), input('Repo Code: '), input('Org Code: '), input('Image URL: '),input('URL: '))
        print(json.dumps(repo, sort_keys: False, indent: 4))
```

--

FIXME: remaining slides need to be written to lesson plan.

# 4. Repositories

+ List all repositories descriptions
+ List a specific repository description
+ Update a repository
+ Delete a repository

--


# Working with Agents

+ Creating two Agents
+ View an Agent details
+ Update an Agent
+ List Agents ID
+ Delete an Agent

--

# Working with Accessions

+ Creating two Accessions
+ Viewing Accession details
+ Updating an Accession
+ Listing Accession IDs
+ Deleting an Accession

--

# Working in batches

+ getting a list of useful IDs
+ iterating over the IDs
+ managing process load
    + avoiding too much of a good thing

--

#  Other ArchivesSpace models

+ Digital Objects
+ Resources
+ Subjects/Terms

--

# References

+ [ArchivesSpace REST API](http://archivesspace.github.io/archivesspace/api/)
+ [Python 3 Docs](https://docs.python.org/3.5/)
    + [urllib2](https://docs.python.org/3/howto/urllib2.html)
        + [Basic Auth example](http://www.voidspace.org.uk/python/articles/authentication.shtml)
    + [JSON module](https://docs.python.org/3.5/library/json.html?highlight=json#module-json)
    + [OS module](https://docs.python.org/3.5/library/os.html) (for using environment variables)
+ [github.com/caltechlibrary/aspace-api-workshop](https://github.com/caltechlibrary/aspace-api-workshop)

--

Thank you

Presentation is at 

[rsdoiel.github.io/archivesspace-api-workshop](https://rsdoiel.github.io/archivesspace-api-workshop)

Slides can be downloaded at

[github.com/rsdoiel/archivesspace-api-workshop/releases/latest](https://github.com/rsdoiel/archivesspace-api-workshop/releases/latest)

Please feel free to fork and improve.

