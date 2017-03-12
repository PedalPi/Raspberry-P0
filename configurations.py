from gpiozero.pins.mock import MockPin

from raspberry_p0.component.seven_segments_display import SevenSegmentsDisplay
from raspberry_p0.component.patch_component import PatchComponent

import json
from configparser import ConfigParser

class Configurations(object):
    """
    Configure the pins based in BCM pinout number.
    See https://pinout.xyz/ for help
    """

    def __init__(self, configuration_file):
        self.display = None
        self.next_patch_button = None
        self.before_patch_button = None

        config = self._parse_configuration(configuration_file)
        config = self._prepare_pins(config)
        self.configure(config)

    def _parse_configuration(self, configuration_file):
        config_parser = ConfigParser()
        config_parser.read(configuration_file)

        data = config_parser['DEFAULT']

        keys = data.keys()

        config = dict()
        config['test'] = config_parser['test']['test'] == 'True'

        config['display'] = dict()
        pin_keys = filter(lambda key: key.startswith('pin_'), keys)
        for key in pin_keys:
            config['display'][key] = int(data[key])

        config['display_common'] = json.loads(data['common_pins'])

        config['next_pedalboard'] = int(data['next_pedalboard'])
        config['before_pedalboard'] = int(data['before_pedalboard'])

        return config

    def _prepare_pins(self, config):
        test = config['test']

        if not test:
            return config

        for key, value in config['display'].items():
            config['display'][key] = MockPin(value)

        new_common = []
        for common in config['display_common']:
            new_common.append(MockPin(common))

        config['display_common'] = new_common

        config['next_pedalboard'] = MockPin(config['next_pedalboard'])
        config['before_pedalboard'] = MockPin(config['before_pedalboard'])

        return config

    def configure(self, config):
        display_pins = config['display']
        self.display = SevenSegmentsDisplay(
            a=display_pins['pin_a'],
            b=display_pins['pin_b'],
            c=display_pins['pin_c'],
            d=display_pins['pin_d'],
            e=display_pins['pin_e'],
            f=display_pins['pin_f'],
            g=display_pins['pin_g'],
            dp=display_pins['pin_dp'],
            common=config['display_common'],
        )

        self.next_patch_button = PatchComponent(config['next_pedalboard'])
        self.before_patch_button = PatchComponent(config['before_pedalboard'])
