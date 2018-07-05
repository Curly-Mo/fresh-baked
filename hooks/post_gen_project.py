#!/usr/bin/env python

import os
import pathlib
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
project_dir = pathlib.Path(PROJECT_DIRECTORY)


class bcolors:
    COMMAND = '\33[32m'
    TEXT = '\33[36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


if __name__ == '__main__':
    print('Creating git repository')
    subprocess.check_call(['git', 'init', '.'])
    subprocess.check_call(['git', 'add', '.'])

    # Add a dir for sphinx
    staticdir = project_dir / 'docs/_static/'
    try:
        staticdir.mkdir()
    except FileExistsError:
        pass

    sh_newline = '\\\n     '
    print("\n")
    print("To finish up, run the following commands")
    print("{}cd{} {{ cookiecutter.project_slug }}/".format(bcolors.COMMAND, bcolors.END))
    print('{}curl{} -u {} https://api.github.com/user/repos {}-d {}{}"name":"{}","description":"{}"{}{}'
          .format(
              bcolors.COMMAND,
              bcolors.END,
              bcolors.TEXT + "'{{ cookiecutter.github_username }}'" + bcolors.END,
              sh_newline,
              "'{",
              '{{ cookiecutter.github_repository_name }}',
              "'" + sh_newline + "'",
              '{{ cookiecutter.project_short_description }}',
              "}'",
              bcolors.END))
    print("{}git{} commit -m {}'initial files'{}".format(
        bcolors.COMMAND, bcolors.END, bcolors.TEXT, bcolors.END))
    print('{}git{} remote add origin {}'.format(
        bcolors.COMMAND, bcolors.END,
        'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.git'
    ))
    print("{}git{} push origin master".format(bcolors.COMMAND, bcolors.END))
