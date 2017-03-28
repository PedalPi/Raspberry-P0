from application.controller.current_controller import CurrentController
from application.controller import effect_controller


class ActionsFacade(object):
    TOKEN = 'raspberry-p0-token'

    def __init__(self, application):
        self.app = application

    @property
    def current_pedalboard(self):
        controller = self.app.controller(CurrentController)
        return controller.current_pedalboard

    def to_next_pedalboard(self):
        controller = self.app.controller(CurrentController)

        controller.to_next_pedalboard(ActionsFacade.TOKEN)
        return controller.current_pedalboard

    def to_before_pedalboard(self):
        controller = self.app.controller(CurrentController)

        controller.to_before_pedalboard(ActionsFacade.TOKEN)
        return controller.current_pedalboard

    def toggle_status_effect(self, effect):
        controller = self.app.controller(effect_controller)
        controller.toggleStatus(effect, ActionsFacade.TOKEN)

    def set_param_value(self, param, new_value):
        effect = param.effect
        controller = self.app.controller(CurrentController)
        controller.setEffectParam(effect.index, param.index, new_value, ActionsFacade.TOKEN)
