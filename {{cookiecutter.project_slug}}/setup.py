"""Setup config is defined in setup.cfg"""

import setuptools

setuptools.setup(
    setup_requires=[],
    setup_cfg=True,
    tests_require=[
        'pytest',
        'pytest-cov',
        'python-coveralls',
        'flake8',
        'pylint',
    ],
)
