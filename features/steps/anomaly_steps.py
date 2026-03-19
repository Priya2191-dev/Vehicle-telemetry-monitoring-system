from behave import given, when, then
from anomaly import detect_anomaly

@given('anomaly data {values}')
def step_impl(context, values):
    context.data = [int(v) for v in values.split(",")]

@when('I check anomaly')
def step_impl(context):
    context.result = detect_anomaly(context.data)

@then('anomaly should be {expected}')
def step_impl(context, expected):
    assert context.result == (expected == "True")
