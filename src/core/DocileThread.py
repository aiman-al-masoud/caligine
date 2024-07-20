from threading import Thread
from typing import Any, Callable, List


class DocileThread(Thread):

    '''
    A thread whose exceptions can be handled from the
    caller thread via join.
    '''

    def __init__(self, fun: Callable, args: List[Any]):

        Thread.__init__(self)
        self.fun = fun
        self.args = args
        self.ex = None
        self.daemon = True

    def run(self):

        try:
            self.fun(*self.args)
        except BaseException as e:
            self.ex = e

    def join(self):

        Thread.join(self)

        if self.ex:
            raise self.ex
