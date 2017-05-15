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

from physical.navigation.view import View
from raspberry_p0.component.components import Components


class PedalboardsView(View):
    controller = None

    display = None
    next_pedalboard = None
    before_pedalboard = None

    def init(self, controller):
        self.controller = controller

    def init_components(self, components):
        self.display = components[Components.DISPLAY]

        self.next_pedalboard = components[Components.NEXT_PEDALBOARD]
        self.before_pedalboard = components[Components.BEFORE_PEDALBOARD]

    def init_components_actions(self):
        self.next_pedalboard.action = self.controller.to_next_pedalboard
        self.before_pedalboard.action = self.controller.to_before_pedalboard

    def show_pedalboard(self, pedalboard):
        self.display.show_pedalboard(pedalboard)
