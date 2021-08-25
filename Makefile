clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

deps:
	poetry install

test: deps
	poetry run pytest -vvv

build: test
	poetry publish -r packagr --build

version = `cat CHANGES.rst | awk '/^[0-9]+\.[0-9]+(\.[0-9]+)?/' | head -n1`


release: clean build
	git rev-parse --abbrev-ref HEAD | grep '^master$$'
	git tag $(version)
	git push origin $(version)

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

pyformat:
	black .

update:
	poetry update
