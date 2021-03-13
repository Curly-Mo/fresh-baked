import os
import subprocess
import tempfile
from cookiecutter.main import cookiecutter
"""
hacky script to run cookiecutter and then run tox for the new project
"""


def main():
    try:
        os.environ['CI']  # is continus integration ?
    except KeyError:
        cookie_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    else:
        cookie_path = os.environ['TRAVIS_BUILD_DIR']

    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        cookiecutter(
            cookie_path,
            no_input=True,
        )

        os.chdir('fresh_baked_skeleton')
        subprocess.check_call(['poetry', 'run', 'tox', '-vv'])


if __name__ == '__main__':
    main()
