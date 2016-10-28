# -*- coding: utf-8 -*-
from physical.mvc.controller import Controller
from raspberry_p0.mvc.patches.patches_view import PatchesView


class PatchesController(Controller):
    index_effect_focused = 0
    current_patch = None

    def __init__(self, controllers, components, actions, observer):
        super().__init__(controllers, components, actions, observer, PatchesView)

    def init(self, current_patch):
        self.current_patch = current_patch
        self.view.show_patch(current_patch)

    def on_current_patch_change(self, patch, token=None):
        self.init(patch)

    def to_next_patch(self):
        next_patch = self.actions.to_next_patch()
        self.init(next_patch)

    def to_before_patch(self):
        before_patch = self.actions.to_before_patch()
        self.init(before_patch)
