.PHONY: main test lint

PYTHON_SCRIPTS_LIST := $(shell find . -type f -name "*.py")
PYTHON ?= python
PYTEST ?= pytest

all: main

main:
	$(PYTHON) main.py

test:
	$(PYTEST)

lint:
	- $(PYTHON) -m pylint --rcfile=.pylintrc $(PYTHON_SCRIPTS_LIST) || true