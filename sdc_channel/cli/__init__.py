import click

from sdc_channel import init
from sdc_channel.version import __version__, __build_time__
from sdc_channel.cli.app import create


@click.group(invoke_without_command=True)
@click.option('-v', '--version', is_flag=True, default=False)
def sc(version):
    if version:
        click.echo('StreamSets Channel version ' + __version__)
        click.echo('Build Time (UTC): ' + __build_time__)


def cli_entry_point():
    init.init()
    sc()


sc.add_command(create)
