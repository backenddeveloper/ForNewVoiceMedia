from cli.exceptions import FinishedException
from cli.view import View


class Subtraction:

    def __init__(self, arguments):
        self.arguments = arguments
        self.message = View.render('subtraction_usage')

    def dispatch(self, stdin):
        stdin = stdin.readline().replace('\n', '')
        try:
            if int(stdin) < 0:
                self.message = View.render('subtraction_validation_error')
                return self
        except ValueError:
                self.message = View.render('subtraction_validation_error')
                return self
        else:
            '''
            Here we use mapreduce to subtract from each number in the arguments
            '''
            self.message = map(lambda x: int(x) - int(stdin), self.arguments)
            self.message = View.render('output', self.message)
            raise FinishedException
