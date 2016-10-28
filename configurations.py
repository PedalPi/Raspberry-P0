from gpiozero.pins.mock import MockPin

from raspberry_p0.component.seven_segments_display import SevenSegmentsDisplay
from raspberry_p0.component.patch_component import PatchComponent


class Configurations(object):
    """
    Configure the pins based in BCM pinout number.
    See https://pinout.xyz/ for help
    """
    display = None
    next_patch_button = None
    before_patch_button = None

    def __init__(self, test=False):
        if test:
            self.test()
        else:
            self.configure()

    def configure(self):
        self.display = SevenSegmentsDisplay(a=13, b=6, c=16, d=20, e=21, f=19, g=26, dp=0, common_unit=5, common_tens=1)

        self.next_patch_button = PatchComponent(14)
        self.before_patch_button = PatchComponent(15)

    def test(self):
        self.display = SevenSegmentsDisplay(
            a=MockPin(13), b=MockPin(6), c=MockPin(16),
            d=MockPin(20), e=MockPin(21), f=MockPin(19),
            g=MockPin(26), dp=MockPin(0),
            common_unit=MockPin(5),
            common_tens=MockPin(1)
        )

        self.next_patch_button = PatchComponent(MockPin(15))
        self.before_patch_button = PatchComponent(MockPin(18))
