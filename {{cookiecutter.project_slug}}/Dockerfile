FROM python:3.6

MAINTAINER {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# create application directory
RUN mkdir /app
WORKDIR /app

COPY pyproject.* ./

# copy project directory
COPY {{ cookiecutter.project_slug }}/ {{ cookiecutter.project_slug }}/

# install dependencies:
RUN poetry install -n --no-dev

# Run everything with poetry env
ENTRYPOINT  [ "poetry", "run"]
