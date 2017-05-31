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

from application.application import Application
from raspberry_p0.raspberry_p0 import RaspberryP0

application = Application(path_data="data/", address='localhost', test=True)

p0 = RaspberryP0(application, configuration_file='config_test.ini')

application.register(p0)
application.start()

application.stop()
