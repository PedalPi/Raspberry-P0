from physical.component.sevensegments.seven_segments import SevenSegmentsBoard


class SevenSegmentsDisplay(object):

    def __init__(self, a, b, c, d, e, f, g, dp, common_unit, common_tens):
        self.board = SevenSegmentsBoard(a=a, b=b, c=c, d=d, e=e, f=f, g=g)
        self.board.add_display(common=common_unit, anode=False)
        self.board.add_display(common=common_tens, anode=True)

    def show_patch(self, patch):
        if patch is None:
            self.board.value = '--'
        else:
            self.board.value = patch.index
