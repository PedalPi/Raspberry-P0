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

from application.component.application_observer import ApplicationObserver
from pluginsmanager.model.update_type import UpdateType
from raspberry_p0.action.actions_facade import ActionsFacade


class P0ApplicationObserver(ApplicationObserver):

    def __init__(self, actions):
        super().__init__()
        self.controller = None
        self.actions = actions

    @property
    def token(self):
        return ActionsFacade.TOKEN

    def register(self, controller):
        self.controller = controller

    def on_current_pedalboard_changed(self, pedalboard, token=None):
        if token != self.token:
            self.controller.on_current_pedalboard_changed(pedalboard)

    def on_bank_updated(self, bank, update_type, index, origin, token=None, **kwargs):
        pass

    def on_pedalboard_updated(self, pedalboard, update_type, index, origin, token=None, **kwargs):
        if token != self.token \
        and update_type == UpdateType.UPDATED \
        and self.actions.current_pedalboard == pedalboard:
            self.controller.on_current_pedalboard_changed(pedalboard)

    def on_effect_updated(self, effect, update_type, index, origin, token=None, **kwargs):
        pass

    def on_effect_status_toggled(self, effect, token=None, **kwargs):
        pass

    def on_param_value_changed(self, param, token=None, **kwargs):
        pass

    def on_connection_updated(self, connection, update_type, pedalboard, token=None, **kwargs):
        pass
