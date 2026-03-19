from behave import when, then
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

@when('I call speed API')
def step_impl(context):
    context.response = client.get("/speed")

@then('response should contain average')
def step_impl(context):
    assert context.response.status_code == 200
    assert "average" in context.response.json()

@when('I call health API')
def step_impl(context):
    context.response = client.get("/health")

@then('status should be running')
def step_impl(context):
    assert context.response.json()["status"] == "running"
