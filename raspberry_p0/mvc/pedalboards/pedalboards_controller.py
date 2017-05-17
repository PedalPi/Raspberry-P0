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

from raspberry_p0.mvc.controller import Controller
from raspberry_p0.mvc.pedalboards.pedalboards_view import PedalboardsView


class PedalboardsController(Controller):

    def __init__(self, controllers, components, actions, observer):
        super().__init__(controllers, components, actions, observer, PedalboardsView)
        self.current_pedalboard = None

    def init(self, current_pedalboard):
        self.current_pedalboard = current_pedalboard
        self.view.show_pedalboard(current_pedalboard)

    def on_current_pedalboard_changed(self, pedalboard):
        self.init(pedalboard)

    def to_next_pedalboard(self):
        next_pedalboard = self.actions.to_next_pedalboard()
        self.init(next_pedalboard)

    def to_before_pedalboard(self):
        before_pedalboard = self.actions.to_before_pedalboard()
        self.init(before_pedalboard)
