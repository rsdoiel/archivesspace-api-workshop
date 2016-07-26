#
# Simple Makefile to generated website and presentation slides
#
build: 
	./mk-website.sh

status:
	git status

release:
	./mk-release.sh

save:
	git commit -am draft
	git push origin master

publish:
	./mk-website.sh
	./mk-release.sh
	./publish.sh

clean:
	if [ -f 00-ArchivesSpace-API-Workshop.html ]; then rm ??-ArchivesSpace-API-Workshop.html; fi
	if [ -f index.html ]; then rm index.html; fi
	if [ -f abstract.html ]; then rm abstract.html; fi
	if [ -f archivesspace-dev/index.html ]; then rm archivesspace-dev/index.html; fi
	if [ -f archivesspace-dev/install.html ]; then rm archivesspace-dev/install.html; fi
	if [ -f archivesspace-api-workshop-slides.zip ]; then rm archivesspace-api-workshop-slides.zip; fi

test:
	python3 login.py
	python3 repo.py
	#python3 agent.py
