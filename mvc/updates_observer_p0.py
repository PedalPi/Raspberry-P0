from application.model.UpdatesObserver import UpdatesObserver
from raspberry_p0.action.actions_facade import ActionsFacade


class UpdatesObserverP0(UpdatesObserver):

    def __init__(self):
        super().__init__()
        self.controller = None
        self.token = ActionsFacade.TOKEN

    def register(self, controller):
        self.controller = controller

    def onCurrentPatchChange(self, patch, token=None):
        self.controller.on_current_patch_change(patch, token)

    def onBankUpdate(self, bank, update_type, token=None):
        self.controller.on_bank_update(bank, update_type, token)

    def onPatchUpdated(self, patch, update_type, token=None):
        self.controller.on_patch_updated(patch, update_type, token)

    def onEffectUpdated(self, effect, update_type, token=None):
        self.controller.on_effect_updated(effect, update_type, token)

    def onEffectStatusToggled(self, effect, token=None):
        self.controller.on_effect_status_toggled(effect, token)

    def onParamValueChange(self, param, token=None):
        self.controller.on_param_value_change(param, token)
