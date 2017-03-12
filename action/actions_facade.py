from application.controller import current_controller
from application.controller import effect_controller


class ActionsFacade(object):
    TOKEN = 'raspberry-p0-token'

    def __init__(self, application):
        self.app = application

    @property
    def current_patch(self):
        controller = self.app.controller(current_controller)
        return controller.current_patch

    def to_next_patch(self):
        controller = self.app.controller(current_controller)

        controller.to_next_patch(ActionsFacade.TOKEN)
        return controller.current_patch

    def to_before_patch(self):
        controller = self.app.controller(current_controller)

        controller.to_before_patch(ActionsFacade.TOKEN)
        return controller.current_patch

    def toggle_status_effect(self, effect):
        controller = self.app.controller(effect_controller)
        controller.toggleStatus(effect, ActionsFacade.TOKEN)

    def set_param_value(self, param, new_value):
        effect = param.effect
        controller = self.app.controller(current_controller)
        controller.setEffectParam(effect.index, param.index, new_value, ActionsFacade.TOKEN)
