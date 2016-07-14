#
# Simple Makefile to generated website and presentation slides
#
build: index.html abstract.html ArchivesSpace-API-Workshop

index.html: README.md page.shorthand nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: README.md" page.shorthand > index.html

abstract.html: Abstract.md page.shorthand nav.md footer.md header.md
	shorthand -e "{{content}} :import-markdown: Abstract.md" page.shorthand > abstract.html

ArchivesSpace-API-Workshop:  ArchivesSpace-API-Workshop.md
	md2slides ArchivesSpace-API-Workshop.md

clean:
	if [ -f 00-ArchivesSpace-API-Workshop.html ]; then rm ??-ArchivesSpace-API-Workshop.html; fi
	if [ -f index.html ]; then rm index.html; fi
	if [ -f abstract.html ]; then rm abstract.html; fi

