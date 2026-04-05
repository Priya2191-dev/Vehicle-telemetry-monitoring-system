import os
import pytest
from telemetry import plot_data

FILE_NAME = "plot.png"

def cleanup():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

def test_plot_creation():
    cleanup()

    plot_data([10, 20, 30], [5, 10, 15])

    assert os.path.exists(FILE_NAME)

    cleanup()

def test_invalid_input():
    with pytest.raises(ValueError):
        plot_data([], [])

def test_length_mismatch():
    with pytest.raises(ValueError):
        plot_data([10, 20], [5])
