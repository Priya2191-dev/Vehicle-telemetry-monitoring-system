from behave import given, when, then
from speed import monitor_speed


@given('speed data "{values}"')
def step_given_speed(context, values):
    try:
        context.data = [float(v.strip()) for v in values.split(",")]
    except ValueError:
        context.data = values  # pass raw for negative test cases

@when('I monitor speed')
def step_when_monitor(context):
    try:
        context.result = monitor_speed(context.data)
        context.error = None
    except Exception as e:
        context.result = None
        context.error = str(e)

@then('average speed should be "{avg}"')
def step_then_avg(context, avg):
    assert context.result["average"] == float(avg)

@then('max speed should be "{max}"')
def step_then_max(context, max):
    assert context.result["max"] == float(max)

@then('an error should occur')
def step_then_error(context):
    assert context.error is not None, "Expected error but none occurred"
