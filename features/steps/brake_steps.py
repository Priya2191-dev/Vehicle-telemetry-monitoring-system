from behave import given, when, then
from brake import brake_analysis


@given('brake pressure data "{values}"')
def given_data(context, values):
    try:
        context.data = [float(v.strip()) for v in values.split(",")]
    except ValueError:
        context.data = values  # pass raw for error testing

@when('I analyze brake pressure')
def when_analyze(context):
    try:
        context.result = brake_analysis(context.data)
        context.error = None
    except Exception as e:
        context.result = None
        context.error = str(e)

@then('brake output should be "{expected}"')
def then_validate_output(context, expected):
    expected_list = [float(v.strip()) for v in expected.split(",")]
    assert context.result == expected_list, f"Expected {expected_list}, got {context.result}"

