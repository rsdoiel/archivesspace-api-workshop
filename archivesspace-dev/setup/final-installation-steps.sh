#!/bin/bash
#

function assertUsername {
    USERNAME=$1
    ERROR_MSG=$2
    WHOAMI=$(whoami)

    if [ "$USERNAME" = "" ];then
        echo "SCRIPTING error, assertUsername expects a username to be supplied to check."
        exit 1
    fi

    if [ "$WHOAMI" != "$USERNAME" ]; then
        echo "This script should be run as the $USERNAME user."
        if [ "$ERROR_MSG" != "" ]; then
            echo $ERROR_MSG;
        fi
        exit 1
    fi
}

function setupUsers {
    sudo adduser archivesspace
    sudo usermod -G vagrant,archivesspace vagrant
}

#
# Setup MySQL appropriately
#
function setupMySQL {
    cd
    echo "Setup MySQL? [Y/n]"
    read Y_OR_N

    if [ "$Y_OR_N" = "" ] || [ "$Y_OR_N" = "y" ] || [ "$Y_OR_N" = "Y" ]; then
        echo "Setting up MySQL users and creating database"
        sudo systemctl start mysqld.service
        touch archivesspace-mysql-setup.sql
        echo "CREATE DATABASE archivesspace DEFAULT CHARACTER SET utf8;" >> archivesspace-mysql-setup.sql
        echo "GRANT ALL ON archivesspace.* TO 'as'@'localhost' IDENTIFIED BY 'as123';" >> archivesspace-mysql-setup.sql
        echo "FLUSH PRIVILEGES;" >> archivesspace-mysql-setup.sql
        sudo mysql < archivesspace-mysql-setup.sql
        echo "Running the ArchivesSpace setup-database.sh script"
        cd /usr/local/archivesspace
        bash scripts/setup-database.sh
        cd
        # Now make things more secure.
        sudo mysql_secure_installation
        sudo systemctl enable mysqld.service
    else
        echo "Skipping MySQL setup."
    fi
}

#
# Setup ArchivesSpace
#
function setupArchivesSpace {
    # See https://www.youtube.com/watch?v=peRcBYqJHGc&index=19&list=PLJFitFaE9AY_DDlhl3Kq_vFeX27F1yt6I
    # for Video tutorial for similar steps on Cent OS 6.x
    echo "Adding archivesspace."
    REVISION="v1.4.2"
    RELEASE_URL="https://github.com/archivesspace/archivesspace/releases/download/$REVISION/archivesspace-$REVISION.zip"
    ZIP_FILE="$HOME/sync/archivesspace-$REVISION.zip"
    if [ -f "$ZIP_FILE" ]; then
        echo "Using existing $ZIP_FILE"
    else
        echo "Grabbing the ArchivesSpace $REVISION (current stable) release."
        echo "$RELEASE_URL"
        curl -L -k -O --url $RELEASE_URL
    fi
    cd /usr/local/
    echo "Unpacking $ZIP_FILE"
    sudo unzip $ZIP_FILE
    sudo ln -s /usr/local/archivesspace /archivesspace
    # RedHat/centos needs to link with chkconfig, debian does something else..
    sudo chkconfig --add /etc/init.d/archivesspace
    echo "Copy in MySQL Java connection."
    cd /usr/local/archivesspace/lib
    sudo curl -Oq http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/mysql-connector-java-5.1.35.jar
    # Setup MySQL connector for use with ArchivesSpace
    # Update config/config.rb
    cd /usr/local/archivesspace
    sudo chown $USER config/config.rb
    echo 'AppConfig[:db_url] = "jdbc:mysql://localhost:3306/archivesspace?user=as&password=as123&useUnicode=true&characterEncoding=UTF-8"' >> config/config.rb
    echo 'AppConfig[:compile_jasper] = true' >> config/config.rb
    echo 'AppConfig[:enable_jasper] = true' >> config/config.rb

    echo "Update ownership to be archivesspace user."
    sudo chown -R archivesspace.archivesspace /usr/local/archivesspace
    sudo chcon -R -h -t httpd_sys_script_rw_t /usr/local/archivesspace
    # Finally make ArchivesSpace come up on boot as archivesspace user.
    sudo ln -s /usr/local/archivesspace/archivesspace.sh /etc/init.d/archivesspace
    sudo sed --in-place=.original -e "s/ARCHIVESSPACE_USER=/ARCHIVESSPACE_USER=archivesspace/g" /usr/local/archivesspace/archivesspace.sh
    sudo chkconfig --level 3 archivesspace on
}

function setupJasperReportsFonts {
    # Setup Jasper reports Add the TTF fonts required to run them.
    cd
    echo "Downloading the TTF fonts"
    curl -O http://thelinuxbox.org/downloads/fonts/msttcorefonts.tar.gz
    echo "Unpacking the TTF fonts"
    tar zxvf msttcorefonts.tar.gz
    echo "Moving them into /usr/share/fonts/TTF"
    sudo mkdir -p /usr/share/fonts/TTF
    sudo cp msttcorefonts/*.ttf /usr/share/fonts/TTF/
    echo "Updating the font cache"
    sudo fc-cache -fv
}

function setupASpaceSourceCode {
    cd
    mkdir -p src
    cd src
    git clone https://github.com/caltechlibrary/aspace.git
    echo "Source for gospace was installed in $HOME/src/aspace"
    echo "You will need Golang 1.5 or better installed to compile and install it"
    echo "    cd $HOME/src/aspace && make install"
}

function setupGolang {
    # Save the path variable state
    OLD_PATH=$PATH
    cd
    git clone https://github.com/golang/go go1.4
    cd go1.4
    git checkout go1.4.2
    cd src
    ./all.bash
    cd
    export PATH=$HOME/go1.4/bin:$PATH
    git clone https://github.com/golang/go
    cd go
    git checkout go1.5.3
    cd src
    ./all.bash
    # Restore the path variable state
    export PATH=$OLD_PATH
}

function setupNginX {
    # Remove legacy Archive
    sudo cp $HOME/sync/etc/yum.repos.d/nginx.repo /etc/yum.repos.d/
    sudo yum -y remove httpd
    #sudo yum -y update
    sudo yum -y install nginx
    # Add our site's to NingX conf./
    sudo cp -v $HOME/sync/etc/nginx/sites/archivesspace_dev.conf /etc/nginx/conf.d/
    # Now start things up.
    sudo systemctl nginx start
    sudo systemctl nginx enable
}

function setupFinish {
    cd
    mkdir bin
    cp -v $HOME/sync/setup/reset-archivesspace.sh bin/
    cp -vR $HOME/sync/tests ./
    sudo chown -R archivesspace /usr/local/archivesspace
    echo ""
    echo "Web Access:"
    echo "    http://localhost:8089/ -- the backend"
    echo "    http://localhost:8080/ -- the staff interface"
    echo "    http://localhost:8081/ -- the public interface"
    echo "    http://localhost:8090/ -- the Solr admin console"
    #echo "    http://localhost:8000/ -- ArchivesSpace behind NginX"
    echo ""
    echo "Bring up archivespace by "
    echo ""
    echo "    sudo /etc/init.d/archivesspace start"
    echo ""
    #echo "Restart Nginx by "
    #echo ""
    #echo "    sudo systemctl restart nginx"
    #echo ""
    echo "And you're ready to create a new repository, load data, and begin development."
    echo ""
}

#
# Main
#
assertUsername vagrant "Try: sudo su vagrant"
setupUsers
setupArchivesSpace
setupMySQL
setupJasperReportsFonts
#setupNginX
#setupGolang
#setupASpaceSourceCode
setupFinish
