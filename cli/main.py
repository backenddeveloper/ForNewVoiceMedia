import re
from cli.exceptions import ValidationException
from cli.subtraction import Subtraction
from cli.view import View


class Main:


    def __init__(self, arguments):
        self.validate(arguments)
        self.arguments = arguments


    def validate(self, arguments):
        if len(arguments) != 6:
            raise ValidationException('validation_error')
        for argument in arguments:
            if re.match('.*[^1-9].*', argument) or int(argument) < 0:
                raise ValidationException('validation_error')
        self.message = View.render('menu', args=arguments)


    def dispatch(self, stdin):
        valid_promises = [Subtraction]
        try:
            '''
            Here we change the offset of the array to zero indexed and dispatch a new promise
            '''
            return valid_promises[int(stdin) - 1](self.arguments)
        except Exception, exception:
            raise ValidationException('invalid_input')
