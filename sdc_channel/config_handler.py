URL = 'url'
NAME = 'name'
TEMPLATE = 'template'
AUTH = 'auth'
TYPE = 'type'
CONFIG = 'config'
DESTINATION = 'destination'
USER = 'user'
PASSWORD = 'password'


class Config:
    def __init__(self, config: dict):
        self.template_name = config[TEMPLATE][NAME]
        self._init_destination(config[DESTINATION])

    def _init_destination(self, dest: dict):
        self.destination_url = dest[URL]
        self.auth_type = dest[AUTH][TYPE].upper()
        self.user = dest[AUTH][CONFIG][USER]
        self.password = dest[AUTH][CONFIG][PASSWORD]


def replace_destination_url(base_config: dict, config: Config):
    base_config = base_config.copy()
    for stage in base_config['pipelineConfig']['stages']:
        if stage['instanceName'] == 'HTTPClient_01':
            for conf in stage['configuration']:
                if conf['name'] == 'conf.resourceUrl':
                    conf['value'] = config.destination_url
                elif conf['name'] == 'conf.client.authType':
                    conf['value'] = config.auth_type
                elif conf['name'] == 'conf.client.basicAuth.username':
                    conf['value'] = config.user
                elif conf['name'] == 'conf.client.basicAuth.password':
                    conf['value'] = config.password
    return base_config
