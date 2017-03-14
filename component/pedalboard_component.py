from gpiozero import Button


class PedalboardComponent(object):

    def __init__(self, pin):
        self.button = Button(pin, pull_up=True)

    @property
    def action(self):
        return self.button.when_pressed

    @action.setter
    def action(self, data):
        self.button.when_pressed = data
