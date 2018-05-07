import re
from cli.exceptions import ValidationException
from cli.highest import Highest
from cli.lowest import Lowest
from cli.multiplication import Multiplication
from cli.subtraction import Subtraction
from cli.view import View


class Main:


    def __init__(self, arguments):
        self.validate(arguments)
        self.arguments = arguments


    def validate(self, arguments):
        if len(arguments) != 6:
            raise ValidationException('initial_validation_error')
        for argument in arguments:
            if re.match('.*[^1-9].*', argument) or int(argument) < 0:
                raise ValidationException('initial_validation_error')
        self.message = View.render('menu', args=arguments)


    def dispatch(self, stdin):
        promise_classes = [Subtraction, Multiplication, Highest, Lowest]
        try:
            '''
            Here we change the offset of the array to zero indexed and dispatch a new promise
            '''
            return promise_classes[int(stdin) - 1](self.arguments)
        except Exception, exception:
            self.message = View.render('invalid_input')
            return self
