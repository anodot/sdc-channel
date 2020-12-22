import inject
import sdc_client

from sdc_channel import core


def _config(binder):
    binder.bind(sdc_client.IStreamSetsProvider, core.StreamsetsProvider())
    binder.bind(sdc_client.IPipelineProvider, core.PipelineProvider())
    binder.bind(sdc_client.ILogger, core.Logger())


def init():
    inject.configure_once(_config)
