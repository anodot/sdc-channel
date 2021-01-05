import jsonschema

from abc import abstractmethod, ABC
from sdc_channel.config import config

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "destination": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "url": {"type": "string"},
                "auth": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "config": {
                            "type": "object",
                            "properties": {
                                "user": {"type": "string"},
                                "password": {"type": "string"},
                            }
                        }
                    }
                },
            }
        },
        "template": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "path": {"type": "string"},
            }
        }
    },
    "required": []
}


def validate(config_: dict):
    jsonschema.validate(config_, schema)
    # if config.DESTINATION not in config_:
    #     raise ValidationException(f'{config.DESTINATION} not found in the config')
    # if config.TYPE not in config_[config.DESTINATION]:
    #     raise ValidationException(f'{config.DESTINATION} {config.TYPE} not found in the config')
    # _get_validator(config_[config.DESTINATION][config.TYPE]).validate(config_)


class _Validator(ABC):
    def validate(self, config_: dict) -> list:
        errors = self._validate_template(config_)
        errors += self._validate_destination(config_[config.DESTINATION])
        if config.NAME not in config_:
            errors.append(f'{config.NAME} not found in the config')
        return errors

    @staticmethod
    def _validate_template(config_: dict) -> list:
        errors = []
        if config.TEMPLATE not in config_:
            return [f'{config.TEMPLATE} not found in the config']
        template = config_[config.TEMPLATE]
        if config.NAME not in template:
            errors.append(f'{config.TEMPLATE} {config.NAME} not found in the config')
        if config.PATH not in template:
            errors.append(f'{config.TEMPLATE} {config.PATH} not found in the config')
        return errors

    @abstractmethod
    def _validate_destination(self, config_: dict) -> list:
        pass


class _ZendeskValidator(_Validator):
    def _validate_destination(self, destination: dict) -> list:
        errors = []
        if config.URL not in destination:
            errors.append(f'{config.URL} not found in the config')
        errors += self._validate_auth(destination)
        return errors

    @staticmethod
    def _validate_auth(destination: dict) -> list:
        if config.AUTH not in destination:
            return [f'{config.AUTH} not found in the config']
        errors = []
        auth = destination[config.AUTH]
        if config.TYPE not in auth:
            errors.append(f'{config.DESTINATION} {config.AUTH} {config.TYPE} not found in the config')
        if config.CONFIG not in auth:
            errors.append(f'{config.DESTINATION} {config.AUTH} {config.CONFIG} not found in the config')
            return errors
        conf = auth[config.CONFIG]
        if config.USER not in conf:
            errors.append(f'{config.DESTINATION} {config.AUTH} {config.CONFIG} not found in the config')
        if config.PASSWORD not in conf:
            errors.append(f'{config.DESTINATION} {config.AUTH} {config.CONFIG} not found in the config')
        return errors


def _get_validator(type_: str) -> _Validator:
    v = {
        config.ZENDESK: _ZendeskValidator,
    }
    return v[type_]()


class ValidationException(Exception):
    pass
