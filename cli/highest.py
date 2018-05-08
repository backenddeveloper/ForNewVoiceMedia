import re
from cli.exceptions import FinishedException
from cli.view import View

class Highest:

    def __init__(self, arguments):
        arguments = [int(x) for x in arguments]
        arguments.sort()
        arguments.reverse()
        self.message = View.render('output', args=arguments)


    def dispatch(self, stdin):
        self.message = ''
        raise FinishedException
