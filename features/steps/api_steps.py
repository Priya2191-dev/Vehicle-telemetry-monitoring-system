from behave import when, then
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


@when('I call speed API')
def step_speed(context):
    context.response = client.get("/speed")

@when('I call health API')
def step_health(context):
    context.response = client.get("/health")

@when('I call speed API with invalid data')
def step_invalid(context):
    context.response = client.get("/speed?data=fast")

@then('response should contain average')
def step_validate_avg(context):
    assert context.response.status_code == 200
    assert "average" in context.response.json()

@then('status should be running')
def step_validate_health(context):
    assert context.response.status_code == 200
    assert context.response.json()["status"] == "running"

@then('an error should occur')
def step_error(context):
    assert context.response.status_code in [400, 422]
