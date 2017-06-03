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

import os

from gpiozero.pins.mock import MockPin


from raspberry_p0.configurations.configurations_parser import ConfigurationsParser

from configparser import ConfigParser


from abc import ABCMeta, abstractmethod


class Configurations(metaclass=ABCMeta):
    """
    Configure the pins based in BCM pinout number.
    See https://pinout.xyz/ for help
    """

    def __init__(self, configuration_file):
        self._config_parser = self._load_configurations(configuration_file)

    def _load_configurations(self, configuration_file):
        config_parser = ConfigParser()
        config_parser.read(os.path.dirname(__file__) + '/../config.ini')
        if configuration_file is not None:
            config_parser.read(configuration_file)

        return config_parser

    @property
    @abstractmethod
    def schema(self):
        pass

    @abstractmethod
    def configure(self, config):
        """
        :param dict config: Config parsed
        :return: Class contemning elements loaded
        """
        pass

    def load(self):
        test = self._config_parser['test']['test'] == 'True'
        config = ConfigurationsParser(self.schema).parse(self._config_parser, test)

        return self.configure(config)
