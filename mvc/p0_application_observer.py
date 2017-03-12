from application.component.application_observer import ApplicationObserver
from raspberry_p0.action.actions_facade import ActionsFacade


class P0ApplicationObserver(ApplicationObserver):

    def __init__(self):
        super().__init__()
        self.controller = None
        self.token = ActionsFacade.TOKEN

    def register(self, controller):
        self.controller = controller

    def on_current_pedalboard_changed(self, pedalboard, token=None):
        pass

    def on_bank_updated(self, bank, update_type, **kwargs):
        self.controller.on_bank_update(bank, update_type)

    def on_pedalboard_updated(self, pedalboard, update_type, **kwargs):
        self.controller.on_pedalboard_updated(pedalboard, update_type, **kwargs)

    def on_effect_updated(self, effect, update_type, **kwargs):
        self.controller.on_effect_updated(effect, update_type)

    def on_effect_status_toggled(self, effect):
        self.controller.on_effect_status_toggled(effect)

    def on_param_value_changed(self, param):
        self.controller.on_param_value_change(param)

    def on_connection_updated(self, connection, update_type):
        pass
