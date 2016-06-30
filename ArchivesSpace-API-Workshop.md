
# Outline of a ArchivesSpace API workshop

## Requirements

Requirements for participants:

+ A laptop/device with network access
    + Linux (what I use), Mac OS X (which I am familiar with), or Windows (which I am very rusty on)
    + Python 3 installed including the python standard library (see https://docs.python.org/3/library/)
        + Python 3 (v3.5.x) can be downloaded and from https://www.python.org/downloads/
        + We’ll be making heavy use of http, json modules
+ A Text Editor (if they don’t have one I recommend Atom Editor at http://atom.io)
+ A web browser (recommend Firefox or Chrome with the JSONView plugin https://jsonview.com/)
+ Access to ArchivesSpace REST API (will be provided at conference)

Recommended:

Read through https://docs.python.org/3/tutorial/index.html if they are not familiar with Python.
Bookmark in your web browser: http://archivesspace.github.io/archivesspace/api/
Bookmark in your web browser: https://docs.python.org/3/library/index.html



## Before the workshop

+ Install Python 3.5.x if needed
+ Download and install the vagrant instance from https://github.com/caltechlibrary/aspace-api-workshop
+ Install Virtualbox and Vagrant is needed
+ Make sure you can bring up ArchivesSpace in the vagrant configuration
+ Make sure you have Python version 3 available on your laptop


## Workshop

### Overview the API

+ Setting up your Vagrant ArchivesSpace instance
+ Brief explanation of REST and JSON
+ Documentation on the [ArchivesSpace REST API](http://archivesspace.github.io/archivesspace/api/)
    + unfortunately this doesn't come up in Google Searches

### Making contact with the API

+ Starting the Python Development Environment (IDLE)
+ Importing the modules needed for the workshop
+ How to make a web client request in Python
+ How to view the response

### Authenticating

+ Forming your request
+ Understanding the response
+ Remembering the authentication token

#### Repositories

+ Creating two repositories repository
+ View the repository information
+ List the available repositories
+ Deleting a repository

### Working with Agents

+ Creating two Agents
+ View an Agent details
+ Update an Agent
+ List Agents ID
+ Delete an Agent

### Working with Accessions

+ Creating two Accessions
+ Viewing Accession details
+ Updating an Accession
+ Listing Accession IDs
+ Deleting an Accession


### Working in batches

+ getting a list of useful IDs
+ iterating over the IDs
+ managing process load
    + avoiding too much of a good thing

###  Other ArchivesSpace models

+ Digital Objects
+ Resources
+ Subjects/Terms


## References

+ [ArchivesSpace REST API](http://archivesspace.github.io/archivesspace/api/)
+ [Python 3 Docs](https://docs.python.org/3.5/)
    + [urllib2](https://docs.python.org/3/howto/urllib2.html)
        + [Basic Auth example](http://www.voidspace.org.uk/python/articles/authentication.shtml)
    + [JSON module](https://docs.python.org/3.5/library/json.html?highlight=json#module-json)
    + [OS module](https://docs.python.org/3.5/library/os.html) (for using environment variables)
+ [github.com/caltechlibrary/aspace-api-workshop](https://github.com/caltechlibrary/aspace-api-workshop)

## Shameless plug

+ [Caltech Archives Integration Tools Project](http://github.com/caltechlibrary/cait)
