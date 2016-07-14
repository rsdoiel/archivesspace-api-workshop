#
# Simple Makefile to generated website and presentation slides
#
build: index.html abstract.html proposal.html ArchivesSpace-API-Workshop archivesspace-dev/index.html archivesspace-dev/install.html

index.html: README.md page.shorthand nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: README.md" page.shorthand > index.html

abstract.html: Abstract.md page.shorthand nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: Abstract.md" page.shorthand > abstract.html

proposal.html: ArchivesSpace-API-Proposal.md page.shorthand nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: ArchivesSpace-API-Proposal.md" page.shorthand > proposal.html

ArchivesSpace-API-Workshop:  ArchivesSpace-API-Workshop.md
	md2slides ArchivesSpace-API-Workshop.md

archivesspace-dev/index.html: archivesspace-dev/README.md archivesspace-dev/page.shorthand archivesspace-dev/nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: archivesspace-dev/README.md" archivesspace-dev/page.shorthand > archivesspace-dev/index.html

archivesspace-dev/install.html: archivesspace-dev/INSTALL.md archivesspace-dev/page.shorthand archivesspace-dev/nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: archivesspace-dev/INSTALL.md" archivesspace-dev/page.shorthand > archivesspace-dev/install.html

clean:
	if [ -f 00-ArchivesSpace-API-Workshop.html ]; then rm ??-ArchivesSpace-API-Workshop.html; fi
	if [ -f index.html ]; then rm index.html; fi
	if [ -f abstract.html ]; then rm abstract.html; fi
	if [ -f proposal.html ]; then rm proposal.html; fi
	if [ -f archivesspace-dev/index.html ]; then rm archivesspace-dev/index.html; fi
	if [ -f archivesspace-dev/install.html ]; then rm archivesspace-dev/install.html; fi

