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

from application.controller.current_controller import CurrentController
from application.controller import effect_controller


class ActionsFacade(object):
    TOKEN = 'raspberry-p0-token'

    def __init__(self, application):
        self.app = application

    @property
    def current_pedalboard(self):
        controller = self.app.controller(CurrentController)
        return controller.current_pedalboard

    def to_next_pedalboard(self):
        controller = self.app.controller(CurrentController)

        controller.to_next_pedalboard(ActionsFacade.TOKEN)
        return controller.current_pedalboard

    def to_before_pedalboard(self):
        controller = self.app.controller(CurrentController)

        controller.to_before_pedalboard(ActionsFacade.TOKEN)
        return controller.current_pedalboard

    def toggle_status_effect(self, effect):
        controller = self.app.controller(effect_controller)
        controller.toggleStatus(effect, ActionsFacade.TOKEN)

    def set_param_value(self, param, new_value):
        effect = param.effect
        controller = self.app.controller(CurrentController)
        controller.setEffectParam(effect.index, param.index, new_value, ActionsFacade.TOKEN)
