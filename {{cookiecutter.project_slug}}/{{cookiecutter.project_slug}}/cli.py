"""Command line interface for {{ cookiecutter.project_slug }}"""
import logging

import click

from {{ cookiecutter.project_slug }} import main


@click.group()
@click.option("-v", "--verbose", count=True)
@click.pass_context
def cli(ctx, verbose):
    ctx.show_default = True
    initLogging(verbose)


@cli.command()
def train():
    click.echo("Perhaps you'll write a train command")
    result = main.main()
    click.echo("Main output: {}".format(result))


@cli.command()
def predict():
    click.echo("Maybe a predict command")
    result = main.main()
    click.echo("Main output: {}".format(result))


def initLogging(verbosity=0):
    """Setup logging with a given verbosity level"""
    # import logging.config
    # logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)
    logging.basicConfig()
    if verbosity == 0:
        logging.root.setLevel(logging.WARN)
    if verbosity == 1:
        logging.root.setLevel(logging.INFO)
    if verbosity > 1:
        logging.root.setLevel(logging.DEBUG)
