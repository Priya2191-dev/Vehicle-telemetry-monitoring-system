from behave import then

@then('an error should occur')
def step_error(context):
    assert context.error is not None, "Expected error but none occurred"
