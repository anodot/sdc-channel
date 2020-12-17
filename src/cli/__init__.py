import click

from src.version import __version__, __build_time__
from src.cli.app import sc_group


@click.group(invoke_without_command=True)
@click.option('-v', '--version', is_flag=True, default=False)
def sc(version):
    if version:
        click.echo('StreamSets Channel version ' + __version__)
        click.echo('Build Time (UTC): ' + __build_time__)


def cli_entry_point():
    sc()


sc.add_command(sc_group)
