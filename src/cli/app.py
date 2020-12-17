import click
import yaml


@click.group(name='sc')
def sc_group():
    pass


@click.command(name='create')
@click.option('-f', '--file', type=click.File())
def create(file):
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)


sc_group.add_command(create)
