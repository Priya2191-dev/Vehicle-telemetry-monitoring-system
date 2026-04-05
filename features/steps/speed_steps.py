from behave import given, when, then
from speed import monitor_speed


@given('speed data "{values}"')
def given_speed(context, values):
    try:
        context.data = [float(v.strip()) for v in values.split(",")]
    except ValueError:
        context.data = values  # pass raw for negative test cases

@when('I monitor speed')
def when_monitor(context):
    try:
        context.result = monitor_speed(context.data)
        context.error = None
    except Exception as e:
        context.result = None
        context.error = str(e)

@then('average speed should be "{avg}"')
def then_avg(context, avg):
    assert context.result["average"] == float(avg)

@then('max speed should be "{max}"')
def then_max(context, max):
    assert context.result["max"] == float(max)

