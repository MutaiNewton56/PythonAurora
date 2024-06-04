
# import classes,dunction or variables file

# file or folder let be lower case.
# import from from a folder then you need
# make the folder a package.

from app8 import *
from animal import *

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

hello()


