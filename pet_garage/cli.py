# pet_garage/cli.py

import sys
sys.path.append('/home/bill/Development/pet_garage')  # Add the path to your project directory

import click
from pet_garage.db import init_db  # Adjusted import

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    init_db()
    click.echo("Initialized the database.")

# Other CLI commands...

if __name__ == '__main__':
    cli()
