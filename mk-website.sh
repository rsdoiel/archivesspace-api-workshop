#!/bin/bash
#

function makePage () {
    page=$1
    nav=$2
    html_page=$3
    echo "Generating $html_page"
    shorthand \
        -e "{{content}} :import-markdown: $page" \
        -e "{{nav}} :import-markdown: $nav" \
        page.shorthand > $html_page
}
# Presentation slides
md2slides -template slide.template ArchivesSpace-API-Workshop.md

# index.html
makePage README.md nav.md index.html

# abstract.html
makePage Abstract.md nav.md abstract.html 

# archivesspace-dev/index.html
makePage archivesspace-dev/README.md archivesspace-dev/nav.md archivesspace-dev/index.html

# archivesspace-dev/install.html
makePage archivesspace-dev/INSTALL.md archivesspace-dev/nav.md archivesspace-dev/install.html

