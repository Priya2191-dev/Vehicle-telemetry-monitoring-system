import os
from telemetry import plot_data

def test_plot_creation():
    speed = [10, 20, 30]
    pressure = [5, 10, 15]

    # Cleanup before test
    if os.path.exists("plot.png"):
        os.remove("plot.png")

    plot_data(speed, pressure)

    assert os.path.exists("plot.png")
