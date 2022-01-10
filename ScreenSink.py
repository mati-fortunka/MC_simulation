from Sink import Sink


class ScreenSink(Sink):

    def __call__(self, *args):
        if isinstance(args[0], str):
            print(args[0])
        else:
            print("Argument should be a string.")
