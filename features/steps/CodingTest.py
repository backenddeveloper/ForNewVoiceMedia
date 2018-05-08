import json
from behave import given, then, when
from mock import MagicMock as Mock

from cli.exceptions import FinishedException, ValidationException
from cli.main import Main
from cli.view import View


def get_stdin(line):
    return Mock(readline=Mock(return_value=line))

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
        context.test_subject = context.test_subject.dispatch(get_stdin(1))
        context.test_subject = context.test_subject.dispatch(get_stdin(number))
    except FinishedException, exception:
        context.output = context.test_subject.message


@when(u'I calculate a the product')
def step_impl(context):
    try:
        context.test_subject = context.test_subject.dispatch(get_stdin(2))
        context.test_subject = context.test_subject.dispatch(get_stdin('testfilename'), open=Mock(return_value=Mock()))
    except FinishedException, exception:
        context.output = context.test_subject.message


@when(u'I order the numbers highest to lowest')
def step_impl(context):
    try:
        context.test_subject = context.test_subject.dispatch(get_stdin(3))
    except FinishedException, exception:
        context.output = context.test_subject.message


@when(u'I order the numbers lowest to highest')
def step_impl(context):
    try:
        context.test_subject = context.test_subject.dispatch(get_stdin(4))
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
    assert context.test_subject.message == View.render('output', args=[ int(x) for x in output.split(', ')])


@then(u'I expect the returned object to be valid JSON')
def step_impl(context):
    json.loads(context.output)


@then(u'that object should contain a key of \'{key}\' and a value of {value:d}')
def step_impl(context, key, value):
    assert json.loads(context.output)[key] == value


@then(u'that object should contain {count:d} keys containing \'{key_part}\'')
def step_impl(context, count, key_part):
    assert len(filter(lambda x: key_part in x, json.loads(context.output).keys())) == count
