import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

def plot_data(speed: List[float], pressure: List[float], filename: str = "plot.png"):
    """
    Generate telemetry plot for speed and pressure.

    Args:
        speed (List[float]): Speed values
        pressure (List[float]): Pressure values
        filename (str): Output plot file
    """

    if not isinstance(speed, list) or not isinstance(pressure, list):
        raise ValueError("Inputs must be lists")

    if not speed or not pressure:
        raise ValueError("Input lists cannot be empty")

    if len(speed) != len(pressure):
        raise ValueError("Speed and pressure length mismatch")

    plt.figure()

    plt.plot(speed, label="Speed")
    plt.plot(pressure, label="Pressure")

    plt.legend()
    plt.title("Telemetry Data")
    plt.xlabel("Time")
    plt.ylabel("Values")

    plt.savefig(filename)
    plt.close()

    logging.info(f"Plot saved as {filename}")
