import os
import subprocess
import sys
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

        version = sys.version_info
        tox_env = 'py{major}{minor}'.format(major=version.major, minor=version.minor)
        os.chdir('fresh_baked_skeleton')
        subprocess.check_call(['tox', '-e', tox_env])


if __name__ == '__main__':
    main()
