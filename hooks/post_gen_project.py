#!/usr/bin/env python

import subprocess

# support python 2.7 input
try:
    input = raw_input
except NameError:
    pass


class colors:
    COMMAND = '\33[32m'
    TEXT = '\33[36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def ask_run(args):
    print('')
    print_args = args[:]
    print_args[0] = colors.COMMAND + print_args[0] + colors.END
    response = input("Execute command: `{}`\n[Y/n]:".format(' '.join(print_args)))
    if response.lower() in ['y', 'yes', '']:
        subprocess.check_call(args)


def print_run(args):
    print('')
    print_args = args[:]
    print_args[0] = colors.COMMAND + print_args[0] + colors.END
    print(' '.join(print_args))
    subprocess.check_call(args)


if __name__ == '__main__':
    print('')
    print('Creating git repository')
    print_run(['git', 'init', '.'])
    print_run(['git', 'add', '.'])

    response = input("Execute post install script? [y/N]:")
    if response.lower() in ['y', 'yes']:
        ask_run([
            'curl', '-u', '{{ cookiecutter.github_username }}', 'https://api.github.com/user/repos', '-d',
            '{"name":"{{ cookiecutter.github_repository_name }}","description":"{{ cookiecutter.project_short_description }}","homepage":"{{ cookiecutter.homepage }}"}'])
        ask_run(['git', 'commit', '-m', 'initial files'])
        ask_run(['git', 'remote', 'add', 'origin', 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.git'])
        ask_run(['git', 'push', 'origin', 'master'])
