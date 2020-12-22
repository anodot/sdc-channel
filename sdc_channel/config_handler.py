URL = 'url'
NAME = 'name'
TEMPLATE = 'template'
PATH = 'path'
AUTH = 'auth'
TYPE = 'type'
CONFIG = 'config'
DESTINATION = 'destination'
USER = 'user'
PASSWORD = 'password'


class Config:
    def __init__(self, config: dict):
        self._init_template(config[TEMPLATE])
        self._init_destination(config[DESTINATION])

    def _init_template(self, template: dict):
        self.template_name = template[NAME]
        with open(template[PATH]) as f:
            self.template = f.read()
            self.template = self.template.replace('\n', '\\n')

    def _init_destination(self, dest: dict):
        self.destination_url = dest[URL]
        self.auth_type = dest[AUTH][TYPE].upper()
        self.user = dest[AUTH][CONFIG][USER]
        self.password = dest[AUTH][CONFIG][PASSWORD]


def add_constants(base_config: dict, constants: dict):
    base_config = base_config.copy()
    for config in base_config['configuration']:
        if config['name'] == 'constants':
            config['value'] = [{'key': key, 'value': val} for key, val in constants.items()]
    return base_config


def replace_destination_url(base_config: dict, config: Config):
    base_config = base_config.copy()
    for stage in base_config['stages']:
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
        elif stage['instanceName'] == 'JythonEvaluator_01':
            for conf in stage['configuration']:
                if conf['name'] == 'initScript':
                    conf['value'] = _get_jython_vars(config)
    return base_config


def _get_jython_vars(config: Config):
    # todo state deprecated?
    return f"state['TEMPLATE'] = '{config.template}';"
