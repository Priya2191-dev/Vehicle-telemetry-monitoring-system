from behave import then

@then('an error should occur')
def then_error(context):
    assert context.response is not None or context.error is not None

    if hasattr(context, "response") and context.response:
        assert context.response.status_code in [400, 422]
    elif hasattr(context, "error") and context.error:
        assert context.error is not None
    else:
        raise AssertionError("No error captured")
