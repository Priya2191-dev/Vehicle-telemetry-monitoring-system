from behave import then

@then('an error should occur')
def step_error(context):
    assert context.error is not None, "Expected error but none occurred"
    
# fast_api
@then('an error should occur')
def step_error(context):
    assert context.response is not None
    assert context.response.status_code in [400, 422]
