from behave import given, when, then
import os
from telemetry import plot_data

FILE_NAME = "plot.png"


@given('speed values "{values}"')
def given_speed(context, values):
    if values.strip() == "":
        context.speed = []
    else:
        context.speed = [float(v.strip()) for v in values.split(",")]

@given('pressure values "{values}"')
def given_pressure(context, values):
    if values.strip() == "":
        context.pressure = []
    else:
        context.pressure = [float(v.strip()) for v in values.split(",")]

@given('speed values ""')
def given_speed_empty(context):
    context.speed = []

@given('pressure values ""')
def given_pressure_empty(context):
    context.pressure = []

@when('I generate telemetry plot')
def when_generate(context):
    try:
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

        plot_data(context.speed, context.pressure)
        context.error = None
    except Exception as e:
        context.error = str(e)

@then('plot file should exist')
def then_validate_plot(context):
    assert os.path.exists(FILE_NAME), "Plot file not created"
