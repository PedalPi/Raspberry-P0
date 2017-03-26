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
                'footswitch_toggle': bool,
            },

            'test': {
                'test': bool
            }
        }

        config_parser = ConfigParser()
        config_parser.read(configuration_file)

        return ConfigurationsParser(schema).parse(config_parser)

    def configure(self, config):
        display_pins = config['display']

        self.display = SevenSegmentsDisplay(
            a=display_pins.get('pin_a', 13),
            b=display_pins.get('pin_b', 6),
            c=display_pins.get('pin_c', 16),
            d=display_pins.get('pin_d', 20),
            e=display_pins.get('pin_e', 21),
            f=display_pins.get('pin_f', 19),
            g=display_pins.get('pin_g', 26),
            dp=display_pins.get('pin_dp', 0),

            common=config.get('common_pins', [5, 1]),
            common_anode=config.get('common_anode', True),
        )

        pedalboard_pins = config['pedalboard']
        toggle = pedalboard_pins.get('footswitch_toggle', True)
        self.next_pedalboard_button = PedalboardComponent(pedalboard_pins.get('next_pedalboard', 14), toggle)
        self.before_pedalboard_button = PedalboardComponent(pedalboard_pins.get('before_pedalboard', 15), toggle)
