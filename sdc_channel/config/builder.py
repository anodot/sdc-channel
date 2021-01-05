import os

from sdc_channel.config import ConfigParams
from sdc_channel.constants import ROOT


def build(base_config: dict, params: ConfigParams) -> dict:
    config = base_config.copy()
    config['title'] = params.name
    _replace_jython(config, params)
    _replace_destination(config, params)
    return config


def _replace_jython(base_config: dict, config_params: ConfigParams):
    for stage in base_config['stages']:
        if stage['instanceName'] == 'JythonEvaluator_02':
            for config in stage['configuration']:
                if config['name'] in 'script':
                    config['value'] = _get_jython(config_params.type)
                elif config['name'] == 'initScript':
                    config['value'] = _get_jython_vars(config_params)


def _replace_destination(base_config: dict, config_params: ConfigParams):
    for stage in base_config['stages']:
        if stage['instanceName'] == 'HTTPClient_01':
            for config in stage['configuration']:
                if config['name'] == 'conf.resourceUrl':
                    config['value'] = config_params.destination_url
                elif config['name'] == 'conf.client.authType':
                    config['value'] = config_params.auth_type
                elif config['name'] == 'conf.client.basicAuth.username':
                    config['value'] = config_params.user
                elif config['name'] == 'conf.client.basicAuth.password':
                    config['value'] = config_params.password


def _get_jython(type_: str) -> str:
    with open(os.path.join(ROOT, 'config', 'jython', f'{type_}.py')) as f:
        return f.read()


def _get_jython_vars(config: ConfigParams):
    return f"state['TEMPLATE'] = '{config.template}';"
