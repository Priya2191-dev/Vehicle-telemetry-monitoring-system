from behave import then

@then('an error should occur')
def then_error(context):

    # Safely check attributes (avoid AttributeError)
    error = getattr(context, "error", None)
    response = getattr(context, "response", None)

    # Case 1: Logic-based error (non-API features)
    if error is not None:
        assert context.error is not None

    # Case 2: API-based error
    elif response is not None:
        assert context.response.status_code in [400, 422]

    else:
        raise AssertionError("No error captured in context")
