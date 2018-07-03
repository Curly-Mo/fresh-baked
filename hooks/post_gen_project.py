#!/usr/bin/env python

import os
import pathlib
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
project_dir = pathlib.Path(PROJECT_DIRECTORY)


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
