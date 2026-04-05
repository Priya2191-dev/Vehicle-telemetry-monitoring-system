from behave import given, when, then
from anomaly import detect_anomaly

@given('anomaly data "{values}"')
def step_given_data(context, values):
    try:
        context.data = [float(v.strip()) for v in values.split(",") if v.strip()] if values else []
    except Exception:
        context.data = values  # keep raw for error case

@when('I check anomaly')
def step_when_check(context):
    try:
        context.result = detect_anomaly(context.data)
        context.error = None
    except Exception as e:
        context.result = None
        context.error = str(e)

@then('anomaly should be "{expected}"')
def step_then_result(context, expected):
    assert context.result == (expected == "True")

