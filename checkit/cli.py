import click

from checkit.app import create_app

@click.group()
def cli():
    pass

@cli.command()
@click.option("--rules", required=True)
def start(rules):
    app = create_app(rules)
    app.run()