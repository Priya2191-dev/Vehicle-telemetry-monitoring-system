from behave import given, when, then
import os
from telemetry import plot_data

FILE_NAME = "plot.png"


@given('speed values "{values}"')
def step_speed(context, values):
    context.speed = [float(v.strip()) for v in values.split(",") if v.strip()] if values else []


@given('pressure values "{values}"')
def step_pressure(context, values):
    context.pressure = [float(v.strip()) for v in values.split(",") if v.strip()] if values else []


@when('I generate telemetry plot')
def step_generate(context):
    try:
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

        plot_data(context.speed, context.pressure)
        context.error = None
    except Exception as e:
        context.error = str(e)


@then('plot file should exist')
def step_validate_plot(context):
    assert os.path.exists(FILE_NAME), "Plot file not created"
