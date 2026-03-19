from behave import given, when, then
from brake import brake_analysis

@given('brake pressure data {values}')
def step_impl(context, values):
    context.data = [int(v) for v in values.split(",")]

@when('I analyze brake pressure')
def step_impl(context):
    context.result = brake_analysis(context.data)

@then('brake output should be {expected}')
def step_impl(context, expected):
    expected_list = [float(v) for v in expected.split(",")]
    assert context.result == expected_list
