from behave import then

@then('an error should occur')
def then_error(context):

    # Safely check attributes (avoid AttributeError)
    response = getattr(context, "response", None)
    error = getattr(context, "error", None)

    # Case 1: API-based error
    if response is not None:
        assert response.status_code in [400, 422]

    # Case 2: Logic-based error (non-API features)
    elif error is not None:
        assert error is not None

    else:
        raise AssertionError("No error captured in context")
