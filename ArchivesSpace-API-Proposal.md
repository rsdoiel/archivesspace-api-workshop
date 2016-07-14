
Good afternoon Christine,

Here’s a tentative outline for a workshop about the ArchivesSpace REST API. I’ve assumed instruction in Python. I would also be comfortable teaching the workshop using JavaScript or PHP if that is preferred.

Requirements
* Laptop (Linux, Mac OS X or Windows)
* * Python 3.5 or better
* * Vagrant and Virtualbox
* * Download the workshop materials
* * ArchivesSpace 1.4.2 (or 1.5 is that is available at that time)
* * A web browser
*
*
* Before the workshop
* * Install Virtualbox and Vagrant if needed
* * Install Python 3.5 if needed
* * Download and install the vagrant instance from https://github.com/caltechlibrary/aspace-api-workshop
* * Make sure you can bring up ArchivesSpace in the vagrant configuration
* * Make sure you have Python version 3 available on your laptop
*
* Overview
* * Setting up your Vagrant ArchivesSpace instance
* * Brief explanation of REST and JSON
* * Documentation on the ArchivesSpace REST API <http://archivesspace.github.io/archivesspace/api/>
*
* Making contact with the API
* * Starting the Python Development Environment (IDLE)
* * Importing the modules needed for the workshop
* * How to make a web client request in Python
* * How to view the response
*
* Authenticating
* * Forming your request
* * Understanding the response
* * Remembering the authentication token
*
* Getting started with a Repository
* * Creating two new repositories
* * View the repository information
* * List the available repositories
* * Deleting a repository
*
* Working with Agents
* * Creating two Agents
* * View an Agent details
* * Update an Agent
* * List Agents ID
* * Delete an Agent
*
* Working with Accessions
* * Creating two Accessions
* * Viewing Accession details
* * Updating an Accession
* * Listing Accession IDs
* * Deleting an Accession
*
* Working in batches
* * getting a list of useful IDs
* * iterating over the IDs
* * managing process load
* * avoiding too much of a good thing
*
*
* Other ArchivesSpace models
* * Digital Objects
* * Resources
* * Subjects/Terms
*
* Where to find more help
* * References materials and links
*
*
*
* Thanks,
*
* Robert
*
* --
* R. S. Doiel, <rsdoiel@caltech.edu>
*
* Digital Library Development
* Caltech Library
*
*
*
*
*
*
* On 3/22/16, 7:09 AM, "Christine Di Bella" <christine.dibella@lyrasis.org> wrote:
*
* Hi Mariella and Robert,
*
* Thanks so much for sending this. At this stage I'm looking for abstracts for the overall workshops/sessions, to which we'll then plug in individual presenters. So this isn't quite what I'm ready for now, but anticipates the next step - not a bad thing! I'm really glad you're interested in presenting about your fabulous work.
*
* Separate from this, on the API we're specifically looking for a description (and instructor) for an API workshop - something that would teach people a little bit about using the API and probably lead them through a few exercises. Robert, if that is something that might be of interest to you, or someone else you know, please let me know.
*
* Thank you!
* Christine
*
* Christine Di Bella
* ArchivesSpace Community Outreach and Support Manager
* christine.dibella@lyrasis.org
* 800.999.8558 x2905
* 678-235-2905
* cdibella13 (Skype)
*
*
* -----Original Message-----
* From: Soprano, Maria (Mariella) [mailto:mariella@caltech.edu]
* Sent: Friday, March 18, 2016 2:58 PM
* To: Christine Di Bella <christine.dibella@lyrasis.org>
* Cc: Doiel, Robert <rsdoiel@caltech.edu>
* Subject: FW: A few sentences on our ArchivesSpace work
*
* Hi Christine,
*
* See below a description of Robert's proposed presentation. Do you need anything else at this stage?
*
* Mariella
*
* -----Original Message-----
* From: Doiel, Robert
* Sent: Friday, March 18, 2016 10:35 AM
* To: Soprano, Maria (Mariella) <mariella@caltech.edu>
* Subject: A few sentences on our ArchivesSpace work
*
* Good Morning,
*
* Not sure if this is what you need. Let me know and I will revise it.
*
* CAIT - Caltech’s ArchivesSpace integration tools
*
* At the Caltech Archives we've adopted ArchivesSpace to managing our archival collections. We chosen to forgo using ArchivesSpace for presenting website.  This was made possible because ArchivesSpace offers a rich REST API.  We have built our own tools around this API allowing us to migrate content, manage content in batch as well as generate website pages and integrate with a custom search engine. It has also enabled the software development staff to move beyond Java or Ruby and develop applications in Go and JavaScript.
*
* Thanks,
*
* Robert
*
* --
* R. S. Doiel, <rsdoiel@caltech.edu>
*
* Digital Library Development
* Caltech Library
*
*
*
