from behave import given, when, then
from speed import monitor_speed

@given('speed data {values}')
def step_impl(context, values):
    context.data = [int(v) for v in values.split(",")]

@when('I monitor speed')
def step_impl(context):
    context.result = monitor_speed(context.data)

@then('average speed should be {avg}')
def step_impl(context, avg):
    assert context.result["average"] == float(avg)

@then('max speed should be {max_val}')
def step_impl(context, max_val):
    assert context.result["max"] == float(max_val)
