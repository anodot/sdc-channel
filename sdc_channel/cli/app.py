import click
import jsonschema
import sdc_client
import yaml

from sdc_channel import core, streamsets_pipelines, config


@click.command()
@click.option('-f', '--file', type=click.File())
def create(file):
    if not file:
        raise click.ClickException('Please specify a file')
    try:
        config_ = yaml.safe_load(file)
        config.validator.validate(config_)
    except yaml.YAMLError as e:
        raise click.ClickException(str(e))
    except jsonschema.exceptions.ValidationError as e:
        raise click.ClickException(f'Config validation failed\n{str(e)}')

    params = config.builder.ConfigParams(config_)
    pipeline = core.Pipeline(
        params.name,
        config.builder.build(core.get_base_config(), params)
    )
    if streamsets_pipelines.exists(pipeline):
        pipeline.set_streamsets(core.StreamSets())
        sdc_client.update(pipeline)
    else:
        sdc_client.create(pipeline)
        streamsets_pipelines.save(streamsets_pipelines.StreamsetsPipeline(pipeline.id, core.StreamSets().get_id()))
        sdc_client.start(pipeline)
