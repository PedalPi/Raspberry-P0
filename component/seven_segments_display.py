from physical.component.sevensegments.seven_segments import SevenSegmentsBoard


class SevenSegmentsDisplay(object):

    def __init__(self, a, b, c, d, e, f, g, dp, common):
        self.board = SevenSegmentsBoard(a=a, b=b, c=c, d=d, e=e, f=f, g=g)
        self.board.add_display(common=common[0], anode=False)
        self.board.add_display(common=common[1], anode=True)

    def show_pedalboard(self, pedalboard):
        if pedalboard is None:
            self.board.value = '--'
        else:
            self.board.value = pedalboard.index
