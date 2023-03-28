APP_NAME ?= DictionarySearch
SHELL := /bin/bash

all: my_program

up:
	python DictionaryQuery/dictionary.py

test:
	cd DictionaryQueryTest && python -m unittest discover

my_program:
	python DictionaryQuery/dictionary.py build