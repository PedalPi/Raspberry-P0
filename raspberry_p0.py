# -*- coding: utf-8 -*-
from application.architecture.Component import Component

from raspberry_p0.mvc.updates_observer_p0 import UpdatesObserverP0

from raspberry_p0.action.actions_facade import ActionsFacade
from raspberry_p0.configurations import Configurations
from raspberry_p0.component.components import Components
from raspberry_p0.mvc.patches.patches_controller import PatchesController


class RaspberryP0(Component):
    """
    Change the current patch with next and before patch
    buttons and view the current patch by SevenSegmentsDisplay

    :param Application application: Class application
    :param string configuration_file: Change the number pins. View raspberry_p0/config.ini for example
    """

    def __init__(self, application, configuration_file="raspberry_p0/config.ini"):
        super(RaspberryP0, self).__init__(application)

        self.app = application
        self.config = Configurations(configuration_file)

        self.components = self.init_components(self.config)
        self.observer = UpdatesObserverP0()
        self.register_observer(self.observer)

        self.actions = ActionsFacade(application)

        self.controllers = self.init_controllers(self.components, self.actions, self.observer)

    def init(self):
        controller = self.controllers[PatchesController]
        controller.start()
        controller.init(self.actions.current_patch)

    def init_components(self, configurations):
        components = dict()

        components[Components.DISPLAY] = configurations.display
        components[Components.NEXT_PATCH] = configurations.next_patch_button
        components[Components.BEFORE_PATCH] = configurations.before_patch_button

        return components

    def init_controllers(self, components, actions, observer):
        controllers = {}

        controllers[PatchesController] = PatchesController(controllers, components, actions, observer)

        return controllers
