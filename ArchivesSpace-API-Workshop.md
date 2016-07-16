
# Introducing the ArchivesSpace REST API using Python 3

+ [R. S. Doiel](https://rsdoiel.github.io)
    + Software Developer 
    + Caltech Library
+ [Mark Custer](https://resources.library.yale.edu/StaffDirectory/detail.aspx?q=702)
    + Archivist and Metadata Coordinator
    + Beinecke Rare Book and Manuscript Library

[Download these slides and examples](./archivesspace-api-workshop-slides.zip)

--

## Requirements

Requirements for participants:

+ A laptop/device with network access
    + Linux (what I use), Mac OS X (which I am familiar with), or Windows (which I am very very rusty on)
    + Python 3 installed including the python standard library (see https://docs.python.org/3/library/)
        + Python 3 (v3.5.2) can be downloaded and from https://www.python.org/downloads/
        + We’ll be making heavy use of urllib and json modules
+ A text Editor
+ A web browser
+ Access to ArchivesSpace REST API
    + The workshop hosts will provide access for Aug 2nd
    + If you have [Virtualbox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) installed
      I have provided [archivesspace-dev](https://github.com/rsdoiel/archivesspace-api-workshop/archivesspace-dev)
+ A basic familiarity with Python

--

## Before the workshop

+ Make sure you have a modern web browser
    + Firefox or Chrome with the [JSONView](https://jsonview.com/) plugin recommented
+ Make sure you have [Python 3.5.2](https://www.python.org/downloads/) 
    + Install [Python 3.5.2](https://www.python.org/downloads/) if needed
+ Make sure you have a text editor
    + IDLE for Python 3 is what I will use in the Workshop
+ A test deployment ArchivesSpace is being provided as part of the Workshop
    + You can install your own via [VirtualBox and Vagrant](http://github.com/rsdoiel/archivesspace-api-workshop/archivesspace-dev/)
+ Recommended reading
    + Read through the [Python 3 tutorial](https://docs.python.org/3/tutorial/index.html) if they are not familiar with Python.
+ Bookmark in your web browser:
    + [ArchivesSpace API Docs](http://archivesspace.github.io/archivesspace/api/)
    + [Python Reference](https://docs.python.org/3/library/index.html)
    + [This presentation website](https://rsdoiel.github.io/archivesspace-api-workshop)

--

# What we'll be covering

+ ArchivesSpace REST API
+ Using Python 3 for interacting with the REST API
+ More generally
    + REST APIs as Data Sources
    + Working with JSON data
+ Identifying helpful web resources for API work

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

+ Open the following in your browser tabs
    + [rsdoiel.github.io/archivesspace-api-workshop](https://rsdoiel.github.io/archivesspace-api-workshop/00-ArchivesSpace-API-Workshop.html) - so you can follow along
    + ArchivesSpace API docs [archivesspace.github.io/archivesspace/api/](http://archivesspace.github.io/archivesspace/api/)
--
# 1. Setup 

## ArchivesSpace

+ Our hosts have provided us with test deployments of ArchivesSpace
    + See hand out or whiteboard for connection details
+ Make sure you can access ArchivesSpace Web UI from your web browser
    + If you've setup a local copy this is usually http://localhost:8080
+ Make sure you can access ArchivesSpace API from your web browser
    + If you've setup a local copy this is usually http://localhost:8089

--


# 1. Setup 

## Python Development Environment

+ Start IDLE for Python 3 
    + confirm the reported version is 3.5.1 or better

--

# 2. Make an http connection

In three parts

+ using the Python interpreter
+ import the urllib and getpass modules
+ make a connection with the request object

--

# 2. Make an http connection

## Let's get started

At this point your setup should be completed and we're
going to start coding in Python 3.

The next set of examples we're go into to run in Python's
shell.

--

# 2. Make an http connection

## launch python

From a terminal on Linux try

```shell
    idle-python3.5 &
```

On Mac OS X or Windows 

1. find your Python 3.5.2 installation folder.
2. find **idle**, click/double click to start it.

--

# 2. Make an http connection

## import modules

Once **idle** starts it'll launch a Python Shell (also known as a Repl).

Type the following in the shell.

```python
    import urllib.request
    import json
    import getpass
```

These are the three modules we'll use through out our Workshop.

--

# 2. Make an http connection

## Create a request object

Continue in the Python shell.

```python
    api_url = 'http://localhost:8089'
    req = urllib.request.Request(api_url)
```

You will need to replace "http://localhost:8089" with your 
Workshop API URL.

This creates a **Request** object named *req*.

--

# 2. Make an http connection

## Make the request, print results

Now we can send our *req* and get back a response.

```python
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('UTF-8'))
```

--

# 2. Make an http connection

## Putting it all together

Put this into a text file called [make-an-http-connection.py](make-an-http-connection.py)

```python
    #!/usr/bin/env python3
    import urllib.request
    import json
    import getpass

    api_url = input('ArchivesSpace API URL: ')
    if api_url == '':
        api_url = 'http://localhost:8089'
    req = urllib.request.Request(api_url)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

```

1. In the text menu click "Run" 
2. click "Run Check"
3. clicl "Run module"

--

# 2. Make an http connection

## If all gone well

1. The shell will have a message saying "RESTART"
2. You'll be prompted for the ArchivesSpace API URL
3. After entering it you'll see the JSON blob response below.

```python
    >>> 
    RESTART: /home/rsdoiel/Sites/archivespace-api-workshop/make-an-http-connection.py 
    ArchivesSpace API URL: http://localhost:8089
    {
       "databaseProductName": "MySQL",
       "databaseProductVersion": "5.6.31",
       "ruby_version": "1.9",
       "host_os": "linux",
       "host_cpu": "x86_64",
       "build": "java1.6",
       "archivesSpaceVersion": "v1.4.2"
    }
    >>> 
```

Now we should be ready to learn how to authenticate with the API.

--

# 3. Authentication

## Basic ingredients

+ Make an http connection
+ Send our username and pasword to the API
+ Save the access token returned

--

# 3. Authentication

## Send our username and password

We need pass our username and password in our request.
We need to keep track of the response. You don't need to
type of the python comments.

Still in the shell type the following (you can skip
the lines starting with '#'

```python
    import urllib.request
    import getpass.getpass

    api_url = input('ArchivesSpace API URL' ) # e.g. http://localhost:8089
    
    username = input('username (e.g. admin): ')
    # We want to use getpass.getpass('password: ') so the
    # password doesn't get echoed to the screen. In IDLE it'll show read and
    # echo the password, ignore this for testing and development.
    password = getpass.getpass('password: ')
```

--

# 3. Authentication

## Send our username and password

Encode our password for sending with our request.

```python
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('utf-8')
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

You should see the type of response ArchivesSpace send back.

--

# 3. Authentication

## Send our username and password

### Putting it all together

Open the IDLE text editor and create an empty
python script called **login-simple.py**. We'll
create a python function and prompt for api url, 
username and password.

```python
    #!/usr/bin/env python3
    import urllib.request
    import getpass
        
    def login (api_url, username, password):
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('utf-8')
        # Notice we're adding the "data" to the url built with Request
        req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        return src
    
    if __name__ == '__main__':
        # this is where we'll test what we're building
        api_url = input('ArchivesSpace API URL: ')
        username = input('ArchivesSpace username: ')
        password = input('ArchivesSpace password: ')
        if api_url == '':
            api_url = 'http://localhost:8089'
        print('Logging in')
        s = login(api_url, username, password)
        print(s)
        print('Success!')
```

Now "Run" the python script and see the results.

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

The session value is our access token. We can pluck that single
item out easiest if we turn the JSON blob into a Python map.

--

# 3. Authentication

1. Save [login-simple.py](login-simple.py) as [login.py](login.py)
2. Open [login.py]
3. You can close the edit window for **login-simply.py**

--

# 3. Authentication

## Save the access token returned

We need to use **import json** and modify our login
function to **parse the JSON response and return 
only session value**. We'll also update our tests at in
the **if __name__ == '__main__':** section at the bottom.

```python
    #!/usr/bin/env python3
    import urllib.request
    import getpass
    import json
        
    def login (api_url, username, password):
        '''This function logs into the ArchivesSpace REST API returning an access token'''
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('utf-8')
        req = urllib.request.Request(api_url+'/users/'+username+'/login', data)
        with urllib.request.urlopen(req) as response:
            src = response.read().decode('UTF-8')
        result = json.JSONDecoder().decode(src)
        return result['session']
    
    if __name__ == '__main__':
        # Our tests
        api_url = input('ArchivesSpace API URL: ')
        if api_url == '':
            api_url = 'http://localhost:8089'
        print('Logging in')
        s = login(api_url, input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
        print("Your access token was: ", s)
        print('Success!')
```

If all has gone well we are ready to move onto working with repositories!

--

# 4. Repositories

## What we'll do in this section

+ Creating two repositories 
    + we'll keep the first and experiment with the second
+ List the available repositories (should see the two we created)
+ View a specific repository 
+ Update a repository
+ Deleting the second repository

--

# 4. Repositories

Creating a repository requires

+ login to API with appropriate account (e.g. admin)
+ package a request to create a repository
+ send the request to create the repository saving the response

We repeat the process to create the second one.

--

# 4. Repositories

## The detailings we need to know

+ Go to [AS REST API docs](http://archivesspace.github.io/archivesspace/api/#get-repositories)
    + We're interested in "Create a Repository"
        + use your browser's find function
+  Look at the example **curl** request on the right


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

(the bit after the "-d" is what we're interested in.)

--

# 4. Repositories

## Creating our create_repo function

The elements we change with each new create request will 
form the parameters in our function. Two elements are required 
and the rest are optional.

### required

+ name
+ repo_code (needs to be unique)

### optional

+ org_code 
+ image_url
+ url

### What we also need

+ We will need to submit our access token and provide the api url too

--

# 4. Repositories

## Use **login.py** as a template script

1. Save [login.py](login.py) As [create-repo.py](create-repo.py)
2. Close **login.py**
3. Open [create-repo.py](create-repo.py)

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
Like *login()* we need to create our data package,
our request object and with "urlopen" get a response.

```python
    def create_repo(api_url, access_token, name, repo_code, org_code = "", image_url = "", url = ""):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = urllib.parse.urlencode({'jsonmodel_type': 'repository',
               'name': name,
               'repo_code': repo_code,
               'org_code': org_code,
               'image_url': image_url,
               'url': url}).encode()
        req = urllib.request.Request(api_url+'/repositories', 
                None, 
                {'X-ArchivesSpace-Session': access_token})
        with urllib.request.urlopen(req, data) as response:
            src = response.read().decode('UTF-8')
        return json.JSONDecoder().decode(src)
```

--

# 4. Repositories

Notice how similar it is to our **login** function. Also how we
add the header to pass along with our request. Some of the important
differences are

+ We're encoding *data* as JSON instead of urlencoding.
+ We've added a our auth token as a header parameter in the *Request*
+ *data* is passed via *urlopen* rather than in our *Request*

```python
    def create_repo(api_url, auth_token, name, repo_code, org_code = "", image_url = "", url = ""):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = json.JSONEncoder().encode({'jsonmodel_type': 'repository',
               'name': name,
               'repo_code': repo_code,
               'org_code': org_code,
               'image_url': image_url,
               'url': url}).encode('utf-8')
        req = urllib.request.Request(api_url+'/repositories', 
                None, 
                {'X-ArchivesSpace-Session': auth_token})
        with urllib.request.urlopen(req, data) as response:
            src = response.read().decode('UTF-8')
        return json.JSONDecoder().decode(src)
```

You can copy and paste your def from our text editor to the repl and make
sure it compiles. 


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
               'url': url}).encode()
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

