
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
6. Change to the sync directory and run the final-installation-step.sh
   - `cd /vagrant && bash setup/final-installation-step.sh`
7. Wait for ArchivesSpace to startup and point your browser at http://localhost:8080 to confirm

### Example local setup

Here's an example of what I would type on my Mac in a Terminal window for the whole process

```
        git clone https://github.com/rsdoiel/archivesspace-api-workshop
        cd archivesspace-api-workshop/archivesspace-dev
        vagrant up
        vagrant ssh
        # At this point I've SSH'd to the vagrante virtual machine instance
        cd /vagrant
        bash setup/final-installation-step.sh
        # This take a little while to run, there are some prompts to answer
        # When complete we'll switch the archivesspace user and start archivesspace
        sudo /etc/init.d/archivesspace start # ArchivesSpace launches daemon, logging is in log/archivesspace.out
```

## Proceed to setup things and import data

Initially ArchivesSpace is configured but lacking data isn't terribly interesting. 
Use your new Python skills to create a repository and add some content.


