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
    print(cookie_path)
    print(os.path.abspath(__file__))
    # extra_context = {
    #     "python_version": sys.version[:3],  # install with travis python V
    # }

    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        cookiecutter(
            cookie_path,
            no_input=True,
        )
            # extra_context=extra_context)
        os.chdir('my_project_name')
        subprocess.check_call(['tox'])


if __name__ == '__main__':
    main()
