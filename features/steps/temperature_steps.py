from behave import given, when, then
from temperature import check_temperature

@given('temperature data {values}')
def step_impl(context, values):
    context.data = [int(v) for v in values.split(",")]

@when('I evaluate temperature')
def step_impl(context):
    context.result = check_temperature(context.data)

@then('status should be {expected}')
def step_impl(context, expected):
    expected_list = expected.split(",")
    assert context.result == expected_list
