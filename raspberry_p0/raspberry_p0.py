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

from application.component.component import Component
from application.controller.current_controller import CurrentController
from application.component.application_observer import ApplicationObserver

from raspberry_p0.config import ConfigurationsRaspberryP0


class RaspberryP0(Component):

    def __init__(self, application, configuration_file=None):
        super(RaspberryP0, self).__init__(application)

        self._observer = ObserverRaspberryP0(self)
        self._current_controller = self.controller(CurrentController)
        self._elements = ConfigurationsRaspberryP0(configuration_file).load()
        print(self._elements)

    def init(self):
        self.register_observer(self._observer)

        self._elements.next_footswitch.action = lambda: self.to_next_pedalboard()
        self._elements.before_footswitch.action = lambda: self.to_before_pedalboard()

        self.show_pedalboard(self._current_controller.pedalboard)

    def close(self):
        self._elements.display.close()

    def to_next_pedalboard(self):
        with self._observer:
            self._current_controller.to_next_pedalboard()
        self.show_current_pedalboard()

    def to_before_pedalboard(self):
        with self._observer:
            self._current_controller.to_before_pedalboard()
        self.show_current_pedalboard()

    def show_pedalboard(self, pedalboard):
        self._elements.display.show_pedalboard(pedalboard)

    def show_current_pedalboard(self):
        self._elements.display.show_pedalboard(self._current_controller.pedalboard)

class ObserverRaspberryP0(ApplicationObserver):

    def __init__(self, raspberry_p0):
        super().__init__()
        self._controller = raspberry_p0

    def on_current_pedalboard_changed(self, pedalboard, **kwargs):
        self._controller.show_pedalboard(pedalboard)

    def on_bank_updated(self, bank, update_type, index, origin, **kwargs):
        pass

    def on_pedalboard_updated(self, pedalboard, update_type, index, origin, **kwargs):
        pass

    def on_effect_updated(self, effect, update_type, index, origin, **kwargs):
        pass

    def on_effect_status_toggled(self, effect, **kwargs):
        pass

    def on_param_value_changed(self, param, **kwargs):
        pass

    def on_connection_updated(self, connection, update_type, pedalboard, **kwargs):
        pass
