from application.application import Application
from raspberry_p0.raspberry_p0 import RaspberryP0

application = Application(data_pedalboard="data/", address='localhost', test=True)

p0 = RaspberryP0(application, configuration_file='config_test.ini')

application.register(p0)
application.start()

p0.close()