import click
import sdc_client
import yaml

from sdc_channel import core
from sdc_channel.config import builder, validator
from sdc_channel.core import Pipeline


@click.command()
@click.option('-f', '--file', type=click.File())
def create(file):
    if not file:
        raise click.ClickException('Please specify a file')
    try:
        config = yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise click.ClickException(str(e))
    validator.validate(config)
    config_params = builder.ConfigParams(config)
    config = builder.build(core.get_base_config(), config_params)
    sdc_client.create(Pipeline(config_params.template_name, config))
