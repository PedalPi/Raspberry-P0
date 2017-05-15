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

from physical.sevensegments.seven_segments import SevenSegmentsBoard


class SevenSegmentsDisplay(object):

    def __init__(self, a, b, c, d, e, f, g, dp, common, common_anode):
        self.board = SevenSegmentsBoard(a=a, b=b, c=c, d=d, e=e, f=f, g=g)
        self.board.add_display(common=common[0], anode=common_anode)
        self.board.add_display(common=common[1], anode=common_anode)

    def show_pedalboard(self, pedalboard):
        if pedalboard is None:
            self.board.value = '--'
        else:
            self.board.value = pedalboard.index

    def close(self):
        self.board.off()
