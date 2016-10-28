from physical.mvc.view import View
from raspberry_p0.component.components import Components


class PatchesView(View):
    controller = None

    display = None
    next_patch = None
    before_patch = None

    def init(self, controller):
        self.controller = controller

    def init_components(self, components):
        self.display = components[Components.DISPLAY]

        self.next_patch = components[Components.NEXT_PATCH]
        self.before_patch = components[Components.BEFORE_PATCH]

    def init_components_actions(self):
        self.next_patch.action = self.controller.to_next_patch
        self.before_patch.action = self.controller.to_before_patch

    def show_patch(self, patch):
        self.display.show_patch(patch)
