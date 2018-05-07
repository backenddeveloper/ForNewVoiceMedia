import re
from cli.view import View

class Main:


    def __init__(self, arguments):
        self.validate(arguments)


    def validate(self, arguments):
        if len(arguments) != 6:
            raise Main.ValidationException('validation_error')
        for argument in arguments:
            if re.match('.*[^1-9].*', argument) or int(argument) < 0:
                raise Main.ValidationException('validation_error')
        self.message = View.render('menu')


    class ValidationException(Exception):


        def __init__(self, message_template):
            self.message = View.render(message_template)
