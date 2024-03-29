# Fresh Baked

[![Build Status](https://travis-ci.com/Curly-Mo/fresh-baked.svg?branch=master)](https://travis-ci.com/Curly-Mo/fresh-baked)
[![License](https://img.shields.io/github/license/Curly-Mo/fresh-baked.svg)](https://github.com/Curly-Mo/fresh-baked/blob/master/LICENSE)


A modern python cookiecutter template

[PEP518](https://www.python.org/dev/peps/pep-0518) approved pyproject.toml, let's start using it for new projects.\
[poetry](https://github.com/sdispater/poetry) is the most well-developed tool so far utilizing pyproject.toml for dependency management, package building, and publishing.\
Together they can fully replace the need for `setup.py`, `setup.cfg`, `pipenv`, `requirements.txt`, `bumpversion`, `twine`...

See an example of what this cookiecutter creates: https://github.com/Curly-Mo/fresh-baked-skeleton

## Features

* Use [poetry](https://github.com/sdispater/poetry) to manage dependencies in ``pyproject.toml`` and deploy to PyPi.
* Choose License: **GPL, MIT, BSD, ISC, Apache**
* **isort, black**: code formatting
* **Pylint, Flake8**: code style
* **pytest**: unit testings
* **pytest-cov**: test coverage reports
* **tox**: for managing tests
* [Click](http://click.pocoo.org/5/why/) for CLI scripts
* **Badges** for [Travis](https://travis-ci.com), [Coveralls](https://coveralls.io), [ReadtheDocs](https://readthedocs.org), [PyPi](https://pypi.org)
* **Travis-CI**: continuous integration
* **Coveralls**: CI coverage reporting
* **Sphinx docs**: Documentation ready for generation and publication to **ReadtheDocs**

## Usage

```console
pip install cookiecutter
cookiecutter https://github.com/Curly-Mo/fresh-baked
```

### Setup integration services
* create your [GitHub](https://github.com) repo
* link your project on [Travis](https://travis-ci.com)
* link your project on [Coveralls](https://coveralls.io)
* link your project on [Read the Docs](https://readthedocs.org)
### Push to GithHub
```console
git commit -m 'intial files'
git remote add origin https://github.com/<github_username>/<github_repo_name>.git
git push origin master
```
Watch as your badges turn :green_heart:green:green_heart:
### Begin development
```console
pip install poetry
poetry install
```

### Tests
```console
poetry run tox
```

### Deploy to PyPi
```console
poetry build
poetry publish
```
