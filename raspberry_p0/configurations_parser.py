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
