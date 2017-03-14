import sys

sys.path.append('.') # raspberry_p0
sys.path.append('../physical')

from application.application import Application
from raspberry_p0.raspberry_p0 import RaspberryP0

application = Application(data_pedalboard="data/", address='localhost', test=True)

p0 = RaspberryP0(application)

application.register(p0)
application.start()

