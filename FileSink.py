from Sink import Sink


class FileSink(Sink):

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__f = open(args[0], "a")
        else:
            print("Argument should be a string.")

    def __call__(self, *args):
        if isinstance(args[0], str):
            self.__f.write(args[0])
        else:
            print("Argument should be a string.")

