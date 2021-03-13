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
    result = runner.invoke(cli.cli, ["--help"])
    assert result.exit_code == 0


def test_cli_train(runner):
    result = runner.invoke(cli.cli, ["-v", "train"])
    assert result.exit_code == 0


def test_cli_predict(runner):
    result = runner.invoke(cli.cli, ["-v", "predict"])
    assert result.exit_code == 0
