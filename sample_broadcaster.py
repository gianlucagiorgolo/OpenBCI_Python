class SampleBroadcaster(object):
    def __init__(self, board, listeners=None):
        self.board = board
        if listeners is None:
            self.liteners = list()
        elif type(listeners) is list:
            self.listeners = listeners
        else:
            self.listeners = list([listeners])

    def add_listener(self, listener):
        self.listeners.append(listener)

    def _broadcast_sample(self, sample):
        for l in self.listeners:
            l.new_sample(sample)

    def start_broadcasting(self):
        self.board.start_streaming(self._broadcast_sample)

    def stop_broadcasting(self):
        self.board.stop()
        self.board.disconnect()

class SampleListener(object):
    def new_sample(self, sample):
        raise NotImplementedError()
