.DEFAULT_GOAL := all

.PHONY: format
format:
	isort .
	black .

.PHONY: lint
lint:
	flake8
	isort  --check-only .
	black --check .

.PHONY: test
test:
	pytest

.PHONY: all
all: test lint
