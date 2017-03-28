import os

from gpiozero.pins.mock import MockPin

from raspberry_p0.component.seven_segments_display import SevenSegmentsDisplay
from raspberry_p0.component.pedalboard_component import PedalboardComponent
from raspberry_p0.configurations_parser import ConfigurationsParser

from configparser import ConfigParser


class Configurations(object):
    """
    Configure the pins based in BCM pinout number.
    See https://pinout.xyz/ for help
    """

    def __init__(self, configuration_file):
        config = self._load_configurations(configuration_file)

        self.display = None
        self.next_pedalboard_button = None
        self.before_pedalboard_button = None

        test = config['test']['test']
        if test:
            self.configure_test(config)
        else:
            self.configure(config)

    def _load_configurations(self, configuration_file):
        schema = {
            'display': {
                'pin_a': int,
                'pin_b': int,
                'pin_c': int,
                'pin_d': int,
                'pin_e': int,
                'pin_f': int,
                'pin_g': int,
                'pin_dp': int,

                'common_pins': list([int]),
                'common_anode': bool,
            },

            'pedalboard': {
                'next_pedalboard': int,
                'before_pedalboard': int,
                'momentary_footswitch': bool,
            },

            'test': {
                'test': bool
            }
        }

        config_parser = ConfigParser()
        config_parser.read(os.path.dirname(__file__) + '/config.ini')
        config_parser.read(configuration_file)

        return ConfigurationsParser(schema).parse(config_parser)

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

            common=display_pins['common_pins'],
            common_anode=display_pins['common_anode'],
        )

        pedalboard_pins = config['pedalboard']
        toggle = pedalboard_pins['momentary_footswitch']

        self.next_pedalboard_button = PedalboardComponent(pedalboard_pins['next_pedalboard'], toggle)
        self.before_pedalboard_button = PedalboardComponent(pedalboard_pins['before_pedalboard'], toggle)

    def configure_test(self, config):
        display_pins = config['display']

        common_pins = [MockPin(pin) for pin in display_pins['common_pins']]
        self.display = SevenSegmentsDisplay(
            a=MockPin(display_pins['pin_a']),
            b=MockPin(display_pins['pin_b']),
            c=MockPin(display_pins['pin_c']),
            d=MockPin(display_pins['pin_d']),
            e=MockPin(display_pins['pin_e']),
            f=MockPin(display_pins['pin_f']),
            g=MockPin(display_pins['pin_g']),
            dp=MockPin(display_pins['pin_dp']),

            common=common_pins,
            common_anode=display_pins['common_anode'],
        )

        pedalboard_pins = config['pedalboard']
        toggle = pedalboard_pins['momentary_footswitch']

        self.next_pedalboard_button = PedalboardComponent(MockPin(pedalboard_pins['next_pedalboard']), toggle)
        self.before_pedalboard_button = PedalboardComponent(MockPin(pedalboard_pins['before_pedalboard']), toggle)
