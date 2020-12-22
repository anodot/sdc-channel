import click
import sdc_client
import yaml

from sdc_channel import config_handler, core
from sdc_channel.core import Pipeline


@click.command()
@click.option('-f', '--file', type=click.File())
def create(file):
    if not file:
        raise click.ClickException('Please specify a file')
    try:
        config = config_handler.Config(yaml.safe_load(file))
    except yaml.YAMLError as e:
        raise click.ClickException(str(e))

    conf = config_handler.replace_destination_url(core.get_base_config(), config)
    sdc_client.create(Pipeline(config.template_name, conf))
