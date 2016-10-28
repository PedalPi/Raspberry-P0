# -*- coding: utf-8 -*-
from application.architecture.Component import Component

from physical.controller.pedal_zero_controller.action.actions_facade import ActionsFacade
from physical.mvc.updates_observer_physical import UpdatesObserverPhysical

from raspberry_p0.configurations import Configurations
from raspberry_p0.component.components import Components
from raspberry_p0.mvc.patches.patches_controller import PatchesController


class RaspberryP0(Component):
    """
    Change the current patch with next and before patch
    buttons and view the current patch by SevenSegmentsDisplay
    """

    def __init__(self, application, test=False):
        super(RaspberryP0, self).__init__(application)

        self.app = application
        self.config = Configurations(test=test)

        self.components = self.init_components(self.config)
        self.observer = UpdatesObserverPhysical()
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
