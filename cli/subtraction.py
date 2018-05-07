import re
from cli.exceptions import FinishedException, ValidationException

class Subtraction:

    def __init__(self, arguments):
        self.arguments = arguments


    def dispatch(self, stdin):
        if re.match('.*[^1-9].*', stdin) or int(stdin) < 0:
            raise ValidationException('validation_error')
        else:
            '''
            Here we use mapreduce to subtract from each number in the arguments
            '''
            self.message = map(lambda x: int(x) - int(stdin), self.arguments)
            raise FinishedException
