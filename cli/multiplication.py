import json
import re
from cli.exceptions import FinishedException
from cli.view import View


class Multiplication:

    def __init__(self, arguments):
        self.arguments = arguments
        self.message = View.render('multiplication_usage')

    def dispatch(self, stdin, open=open):
        stdin = stdin.readline().replace('\n', '')
        if re.search('[^0-9a-zA-Z]', stdin) or len(stdin) < 3:
            self.message = View.render('multiplication_validation_error')
            return self
        else:
            self.message = self.get_output()
            open(stdin + '.json', 'w').write(self.get_output())
            raise FinishedException

    def get_output(self):
        product = reduce(lambda x, y: int(x) * int(y), self.arguments)
        return json.dumps({
            "InputNumber1": self.arguments[0],
            "InputNumber2": self.arguments[1],
            "InputNumber3": self.arguments[2],
            "InputNumber4": self.arguments[3],
            "InputNumber5": self.arguments[4],
            "InputNumber6": self.arguments[5],
            "Multiplication": product
            })
