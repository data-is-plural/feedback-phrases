.PHONY: init archive data 

init:
	git clone https://github.com/data-is-plural/newsletter-archive.git archive

archive:
	cd archive && git pull origin

data:
	python scripts/extract.py

all: archive data
