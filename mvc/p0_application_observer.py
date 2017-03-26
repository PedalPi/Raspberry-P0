from application.component.application_observer import ApplicationObserver
from pluginsmanager.model.update_type import UpdateType
from raspberry_p0.action.actions_facade import ActionsFacade


class P0ApplicationObserver(ApplicationObserver):

    def __init__(self, actions):
        super().__init__()
        self.controller = None
        self.token = ActionsFacade.TOKEN
        self.actions = actions

    def register(self, controller):
        self.controller = controller

    def on_current_pedalboard_changed(self, pedalboard, token=None):
        if token != self.token:
            self.controller.on_current_pedalboard_changed(pedalboard)

    def on_bank_updated(self, bank, update_type, index, origin, token=None, **kwargs):
        pass

    def on_pedalboard_updated(self, pedalboard, update_type, index, origin, token=None, **kwargs):
        if token != self.token \
        and update_type == UpdateType.UPDATED \
        and self.actions.current_pedalboard == pedalboard:
            self.controller.on_current_pedalboard_changed(pedalboard)

    def on_effect_updated(self, effect, update_type, index, origin, token=None, **kwargs):
        pass

    def on_effect_status_toggled(self, effect, token=None, **kwargs):
        pass

    def on_param_value_changed(self, param, token=None, **kwargs):
        pass

    def on_connection_updated(self, connection, update_type, pedalboard, token=None, **kwargs):
        pass
