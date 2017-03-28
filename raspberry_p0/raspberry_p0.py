from application.component.component import Component

from raspberry_p0.mvc.p0_application_observer import P0ApplicationObserver

from raspberry_p0.action.actions_facade import ActionsFacade
from raspberry_p0.configurations import Configurations
from raspberry_p0.component.components import Components
from raspberry_p0.mvc.pedalboards.pedalboards_controller import PedalboardsController


class RaspberryP0(Component):
    """
    Change the current pedalboard with next and before pedalboard
    buttons and view the current pedalboard by SevenSegmentsDisplay

    :param Application application: Class application
    :param string configuration_file: Change the number pins. View raspberry_p0/config.ini for example
    """

    def __init__(self, application, configuration_file="raspberry_p0/config.ini"):
        super().__init__(application)

        self.app = application
        self.config = Configurations(configuration_file)

        self.actions = ActionsFacade(application)

        self.components = self.init_components(self.config)
        self.observer = P0ApplicationObserver(self.actions)
        self.register_observer(self.observer)

        self.controllers = self.init_controllers(self.components, self.actions, self.observer)

    def init(self):
        controller = self.controllers[PedalboardsController]
        controller.start()
        controller.init(self.actions.current_pedalboard)

    def init_components(self, configurations):
        components = dict()

        components[Components.DISPLAY] = configurations.display
        components[Components.NEXT_PEDALBOARD] = configurations.next_pedalboard_button
        components[Components.BEFORE_PEDALBOARD] = configurations.before_pedalboard_button

        return components

    def init_controllers(self, components, actions, observer):
        controllers = {}

        controllers[PedalboardsController] = PedalboardsController(controllers, components, actions, observer)

        return controllers

    def close(self):
        self.config.display.close()
