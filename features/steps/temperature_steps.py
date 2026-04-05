from behave import given, when, then
from temperature import check_temperature


@given('temperature data "{values}"')
def given_temp(context, values):
    try:
        context.data = [float(v.strip()) for v in values.split(",")]
    except ValueError:
        context.data = values  # for negative test


@when('I evaluate temperature')
def when_eval(context):
    try:
        context.result = check_temperature(context.data)
        context.error = None
    except Exception as e:
        context.result = None
        context.error = str(e)


@then('status should be "{expected}"')
def then_status(context, expected):
    expected_list = [v.strip() for v in expected.split(",")]
    assert context.result == expected_list


@then('an error should occur')
def then_error(context):
    assert context.error is not None
