from physical.mvc.controller import Controller
from raspberry_p0.mvc.pedalboards.pedalboards_view import PedalboardsView


class PedalboardsController(Controller):

    def __init__(self, controllers, components, actions, observer):
        super().__init__(controllers, components, actions, observer, PedalboardsView)
        self.current_pedalboard = None

    def init(self, current_pedalboard):
        self.current_pedalboard = current_pedalboard
        self.view.show_pedalboard(current_pedalboard)

    def on_current_pedalboard_change(self, pedalboard, token=None):
        self.init(pedalboard)

    def to_next_pedalboard(self):
        next_pedalboard = self.actions.to_next_pedalboard()
        self.init(next_pedalboard)

    def to_before_pedalboard(self):
        before_pedalboard = self.actions.to_before_pedalboard()
        self.init(before_pedalboard)
