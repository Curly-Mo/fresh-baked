# Fresh Baked

[![Build Status](https://travis-ci.org/Curly-Mo/fresh-baked.svg?branch=master)](https://travis-ci.org/Curly-Mo/fresh-baked)

A modern python cookiecutter template

[PEP518](https://www.python.org/dev/peps/pep-0518) approved pyproject.toml, let's start using it for new projects
[poetry](https://github.com/sdispater/poetry) is the most well-developed tool so far utilizing pyproject.toml for dependency management, package building, and publishing. Together they can fully replace the need for `setup.py`, `setup.cfg`, `pip`, `pipenv`, `requirements.txt`, `bumpversion`, `twine`...

## Features

* Use [poetry](https://github.com/sdispater/poetry) to manage dependencies in ``pyproject.toml`` and deploy to PyPi.
* Choose License: **GPL, MIT, BSD, ISC, Apache**
* **Badges** for [Travis](https://travis-ci.org), [Coveralls](https://coveralls.io), [ReadtheDocs](https://readthedocs.org), [PyUp](https://pyup.io/), [Pypi](https://pypi.org)
* **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**
* **isort, Yapf, black**: code formatting
* **Pylint, Flake8**: code style
* **pytest**: unit testings
* **pytest-cov**: test coverage reports
* **tox**: for managing tests
* **Travis-CI**: continuous integration
* **Coveralls**: CI coverage reporting

## Usage

```console
pip install cookiecutter
cookiecutter https://github.com/Curly-Mo/fresh-baked
```

### Setup integration services
* commit your work!
* create your [GitHub](https://github.com) repo
* link your project on [Travis](https://travis-ci.org)
* link your project on [Coveralls](https://coveralls.io)
* link your project on [Read the Docs](https://readthedocs.org)
* link your project on [PyUp](https://pyup.io/)
### Push to GithHub
```console
git commit -m 'intial files'
git remote add origin https://github.com/<github_username>/<github_repo_name>.git
git push origin master
```
### Begin development
```console
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
poetry install
```

### Tests
```console
poetry run tox
```

## License
[LGPL-3.0](https://github.com/Curly-Mo/fresh-baked/blob/master/LICENSE)
