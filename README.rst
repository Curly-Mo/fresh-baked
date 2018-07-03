.. image:: https://travis-ci.org/Curly-Mo/fresh-baked.svg?branch=master
    :target: https://travis-ci.org/Curly-Mo/fresh-baked


fresh-baked
===================================================
A modern python cookiecutter template

PEP518 approved pyproject.toml, let's start using it (along with poetry) for new projects

This cookiecutter template is inspired from https://github.com/jgirardet/cookiecutter-pipenv

What's included ?
------------------------------

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.


- Use **Poetry** to manage dependencies in ``pyproject.toml`` and deployment to PyPi.
- Free software: **GPL, MIT, ...**
- **Badges** for Travis, Coverage, Pypi, ReadTheDoc
- You choose your vesion of python at install : **3.4, 3.5, 3.6, 3.7**
- **Makefile** to ease daily-life of developers and maintainers
- **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**
- **isort, Yapf, black**: code formatting
- **Pylint, Flake8**: code style
- **pytest**: unit testings
- **pytest-cov**: unit test reports
- **Travis-CI**: build, unit test
- **Coveralls**: CI coverage reporting
- control package security with **pyup**.


Get Started:
--------------

Do not create a folder for your project, it will be automatically created.


    .. code-block:: bash

        $ pip install --user --upgrade cookiecutter

        $ cookiecutter https://github.com/Curly-Mo/fresh-baked

At start it will ask you for libray or app.
This is important depending the way you want dependencies work.
Libray will use Pipfile as requirements.txt, so if put django="\*" the newest version wil be used.
App will use Pipfile.lock as requirements.txt, it will put the exact version you are running (ex : django(1.11.3).
This behaviour tries to do **soft** dependencies for libray but **strong** dependencies for applications.
This will work only if  you use ``make push`` instead of ``git push`` because ``make push`` generates the requirements.txt




Step 2:
---------


Setup for development:
.. code-block:: bash

    $ pip install poetry
    $ poetry install

Step 3:
--------
- commit your work!
- create a github repo
- enable your project on Travis
- enable on read the docs if needed
- enable your coverall account
- enable you pyup account
