from cli.exceptions import FinishedException
from cli.view import View


class Lowest:

    def __init__(self, arguments):
        arguments = [int(x) for x in arguments]
        arguments.sort()
        self.message = View.render('output', args=arguments)

    def dispatch(self, stdin):
        raise FinishedException
