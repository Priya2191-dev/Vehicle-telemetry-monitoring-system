from behave import given, when, then
import os
from telemetry import plot_data

@given('speed values {values}')
def step_impl(context, values):
    context.speed = [int(v) for v in values.split(",")]

@given('pressure values {values}')
def step_impl(context, values):
    context.pressure = [int(v) for v in values.split(",")]

@when('I generate telemetry plot')
def step_impl(context):
    if os.path.exists("plot.png"):
        os.remove("plot.png")
    plot_data(context.speed, context.pressure)

@then('plot file should exist')
def step_impl(context):
    assert os.path.exists("plot.png")
