from gpiozero import Button


class PedalboardComponent(object):

    def __init__(self, pin, toggle=True):
        self.button = Button(pin, pull_up=True)
        self.toggle = toggle

    @property
    def action(self):
        return self.button.when_pressed

    @action.setter
    def action(self, data):
        self.button.when_pressed = data
        if self.toggle:
            self.button.when_released = data
