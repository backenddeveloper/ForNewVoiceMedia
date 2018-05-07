from behave import given, then, when

from cli.exceptions import FinishedException, ValidationException
from cli.main import Main
from cli.view import View


@given(u'I have an input such as {input}')
def step_impl(context, input):
    context.input = input.split(' ')


@when(u'I start a new cli')
def step_impl(context):
    context.test_subject = Main(context.input)


@when(u'I validate it')
def step_impl(context):
    try:
        context.test_subject = Main(context.input)
    except Exception, exception:
        context.exception = exception


@when(u'I subtract a {number:w}')
def step_impl(context, number):
    try:
        context.test_subject = context.test_subject.dispatch(1)
        context.test_subject = context.test_subject.dispatch(number)
    except FinishedException, exception:
        context.output = context.test_subject.message


@then(u'the input validation fails')
def step_impl(context):
    assert hasattr(context, 'exception')


@then(u'a {template} error is returned to the user')
def step_impl(context, template):
    assert context.exception.message == View.render(template, args=context.input)


@then(u'a {template} output is returned to the user')
def step_impl(context, template):
    assert context.test_subject.message == View.render(template, args=context.input)


@then(u'I expect the cli to return {output}')
def step_impl(context, output):
    assert context.test_subject.message == [ int(x) for x in output.split(', ')]
