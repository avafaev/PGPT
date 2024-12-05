.PHONY: build install clean format lint unittest test

build: # force build
	poetry build

install:
	poetry install

format: updatesetup
	isort sspentestlab
	black sspentestlab

updatesetup:
	bash sspentestlab/scripts/update.sh