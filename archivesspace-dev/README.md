
ArchivesSpace is licensed under the [Educational Community License v2](http://opensource.org/licenses/ecl2.php).

# Running ArchivesSpace with Virtualbox/Vagrant

## Initial setup

1. Install Virtualbox
2. Install Vagrant
3. Change to the *archivesspace-dev* directory
    - `cd archivesspace-dev`
4. Bring up vagrant
   - `vagrant up`
5. SSH into vagrant instance
   - `vagrant ssh`
6. Run the *aspace-setup.bash* in /vagrant
   - `/vagrant/aspace-setup.bash`
7. Wait for ArchivesSpace to startup and point your browser at http://localhost:8080 to confirm

### Example local setup

Here's an example of what I would type on my Mac in a Terminal window for the whole process

```
        git clone https://github.com/rsdoiel/archivesspace-api-workshop
        cd archivesspace-api-workshop/archivesspace-dev
        vagrant up
        vagrant ssh
        # At this point I've SSH'd to the vagrante virtual machine instance
        /vagrant/aspace-setup.sh
        # This take a little while to run, there are some prompts to answer
        # When complete we'll switch the archivesspace user and start archivesspace
        sudo /archivesspace/v1.5.0/archivesspace/archivesspace.sh 
        # You can press Ctrl-C to stop ArchivesSpace running
```

## Proceed to setup things and import data

Initially ArchivesSpace is configured but lacking data isn't terribly 
interesting. Use your new Python skills to create a repository and 
add some content.

### Dependencies

+ [Vagrant](https://www.vagrantup.com/) and all that is needed to run vagrant (e.g. [Virtual Box](https://www.virtualbox.org/))
    + [ArchivesSpace](https://github.com/archivesspace/archivesspace/releases/latest) release and its dependencies (this are handled in the VM creation and setup)
+ Bash (for the scripts)


### Reference Material for learning to develop with ArchivesSpace REST API

+ [ArchivesSpace Developer Screencase](https://www.youtube.com/watch?v=z0HR46q4F8o&list=PLJFitFaE9AY_DDlhl3Kq_vFeX27F1yt6I&index=1) the most useful reference to ArchivesSpace's APIs.
+ [REST API Docs](https://archivesspace.github.io/archivesspace/doc/file.API.html) (assumes Ruby and AS JSONModel object, still useful after looking at the screen casts and curl examples)
+ [General documentations](http://archivesspace.github.io/archivesspace/doc/)

