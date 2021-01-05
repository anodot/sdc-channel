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

ZENDESK = 'zendesk'


class ConfigParams:
    def __init__(self, config: dict):
        self.name = config[NAME]
        self._init_template(config[TEMPLATE])
        self._init_destination(config[DESTINATION])

    def _init_template(self, template: dict):
        self.template_name = template[NAME]
        with open(template[PATH]) as f:
            self.template = f.read()
            self.template = self.template.replace('\n', '\\n')

    def _init_destination(self, dest: dict):
        self.destination_url = dest[URL]
        self.type = dest[TYPE]
        self.auth_type = dest[AUTH][TYPE].upper()
        self.user = dest[AUTH][CONFIG][USER]
        self.password = dest[AUTH][CONFIG][PASSWORD]
