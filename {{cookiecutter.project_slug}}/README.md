# {{ cookiecutter.project_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }})
[![Coverage](https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/badge.svg)](https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }})
[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.github_repository_name }}/badge/?version=latest)](https://{{ cookiecutter.github_repository_name }}.readthedocs.org/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.github_repository_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.github_repository_name }})
[![PyPI Pythons](https://img.shields.io/pypi/pyversions/{{ cookiecutter.github_repository_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.github_repository_name }})
[![License](https://img.shields.io/pypi/l/{{ cookiecutter.github_repository_name }}.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/blob/master/LICENSE)

{{ cookiecutter.project_short_description }}

## Features

* What it do?

## Usage

* TODO

## Install

```console
pip install {{ cookiecutter.github_repository_name }}
```

## Documentation
See https://{{ cookiecutter.github_repository_name }}.readthedocs.org/en/latest/

## Development
```console
pip install poetry
cd {{ cookiecutter.github_repository_name }}
poetry install
```
### Run
To run cli entrypoint:
```console
poetry run {{ cookiecutter.project_slug }} --help
```

### Tests
```console
poetry run pytest --cov={{ cookiecutter.project_slug }}
```

### Docker
To run with docker
```console
docker build -t {{ cookiecutter.project_name }}.image .
docker run {{ cookiecutter.project_slug }}.image {{ cookiecutter.project_slug }} --help
```

## License
[{{ cookiecutter.open_source_license}}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/blob/master/LICENSE)
