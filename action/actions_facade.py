from application.controller.CurrentController import CurrentController
from application.controller.EffectController import EffectController


class ActionsFacade(object):
    TOKEN = 'raspberry-p0-token'

    def __init__(self, application):
        self.app = application

    @property
    def current_patch(self):
        controller = self.app.controller(CurrentController)
        return controller.currentPatch

    def to_next_patch(self):
        controller = self.app.controller(CurrentController)

        controller.toNextPatch(ActionsFacade.TOKEN)
        return controller.currentPatch

    def to_before_patch(self):
        controller = self.app.controller(CurrentController)

        controller.toBeforePatch(ActionsFacade.TOKEN)
        return controller.currentPatch

    def toggle_status_effect(self, effect):
        controller = self.app.controller(EffectController)
        controller.toggleStatus(effect, ActionsFacade.TOKEN)

    def set_param_value(self, param, new_value):
        effect = param.effect
        controller = self.app.controller(CurrentController)
        controller.setEffectParam(effect.index, param.index, new_value, ActionsFacade.TOKEN)
