"""
test_cli
----------------------------------
Tests for `cli` module.
"""
import pytest
from click.testing import CliRunner

from {{cookiecutter.project_slug}} import cli

# pylint doesn't like pytest-fixtures
# pylint: disable=redefined-outer-name


@pytest.fixture()
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.cli, ['--verbose'])
    assert result.exit_code == 0
