import json


class ConfigurationsParser(object):
    def __init__(self, schema):
        self.schema = schema

    @property
    def groups(self):
        return self.schema.keys()

    def parse(self, config):
        return self._parse(config, self.schema)

    def _parse(self, element, schema):
        if type(schema) is dict:
            data = {}

            for key in schema.keys():
                try:
                    data[key] = self._parse(element[key], schema[key])
                except KeyError:
                    pass

        elif schema == int:
            data = int(element)

        elif schema == float:
            data = float(element)

        elif schema == bool:
            data = element == 'True'

        elif type(schema) is list:
            data = json.loads(element)

        else:
            data = None

        return data
