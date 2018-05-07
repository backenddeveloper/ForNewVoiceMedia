import re
from cli.exceptions import FinishedException
from cli.view import View

class Lowest:

    def __init__(self, arguments):
        arguments.sort()
        self.message = View.render('output', args=[int(x) for x in arguments])


    def dispatch(self):
        raise FinishedException
