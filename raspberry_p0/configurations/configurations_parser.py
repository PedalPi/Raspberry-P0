# Copyright 2017 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from gpiozero import Pin
from gpiozero.pins.mock import MockPin


class ConfigurationsParser(object):
    def __init__(self, schema):
        self.schema = schema

    def parse(self, config, test=False):
        return self._parse(config, self.schema, test)

    def _parse(self, element, schema, test):
        if type(schema) is dict:
            return self._parse_dict(element, schema, test)

        elif schema == int:
            return int(element)

        elif schema == Pin:
            element_type = MockPin if test else int
            return self._parse(element, element_type, test)

        elif schema == MockPin:
            return MockPin(self._parse(element, int, test))

        elif schema == float:
            return float(element)

        elif schema == bool:
            return element == 'True'

        elif type(schema) is list:
            return self._parse_list(element, schema, test)

        else:
            return None

    def _parse_dict(self, element, schema, test):
        data = {}

        for key in schema.keys():
            try:
                data[key] = self._parse(element[key], schema[key], test)
            except KeyError:
                pass

        return data

    def _parse_list(self, element, schema, test):
        element_type = schema[0]

        data = []
        for e in json.loads(element):
            data.append(self._parse(e, element_type, test))

        return data
