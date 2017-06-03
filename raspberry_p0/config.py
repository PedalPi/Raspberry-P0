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

from gpiozero import Pin

from raspberry_p0.configurations.configurations import Configurations

from raspberry_p0.physical.seven_segments_display import SevenSegmentsDisplay
from raspberry_p0.physical.footswitch import Footswitch


class ConfigurationsRaspberryP0(Configurations):

    @property
    def schema(self):
        return {
            'display': {
                'pin_a': Pin,
                'pin_b': Pin,
                'pin_c': Pin,
                'pin_d': Pin,
                'pin_e': Pin,
                'pin_f': Pin,
                'pin_g': Pin,
                'pin_dp': Pin,

                'common_pins': list([Pin]),
                'common_anode': bool,
            },

            'pedalboard': {
                'next_pedalboard': Pin,
                'before_pedalboard': Pin,
                'momentary_footswitch': bool,
            },

            'test': {
                'test': bool
            }
        }

    def configure(self, config):
        display_pins = config['display']

        display = SevenSegmentsDisplay(
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

        next_pedalboard_button = Footswitch(pedalboard_pins['next_pedalboard'], toggle)
        before_pedalboard_button = Footswitch(pedalboard_pins['before_pedalboard'], toggle)

        return ElementsRaspberryP0(display, before_pedalboard_button, next_pedalboard_button)


class ElementsRaspberryP0(object):

    def __init__(self, display, before_footswitch, next_footswitch):
        self.display = display

        self.before_footswitch = before_footswitch
        self.next_footswitch = next_footswitch
