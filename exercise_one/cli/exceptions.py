from cli.view import View


class ValidationException(Exception):

    def __init__(self, message_template):
        self.message = View.render(message_template)


class FinishedException(Exception):
    pass
