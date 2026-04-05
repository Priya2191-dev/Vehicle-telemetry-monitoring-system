import numpy as np
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

THRESHOLD = 30

def detect_anomaly(data: List[float]) -> bool:
    """
    Detect anomaly based on deviation from mean.

    Args:
        data (List[float]): Input data

    Returns:
        bool: True if anomaly detected
    """

    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    if not data:
        raise ValueError("Data cannot be empty")

    try:
        data = [float(x) for x in data]
    except Exception:
        raise ValueError("All values must be numeric")

    mean = np.mean(data)

    logging.info(f"Data: {data}, Mean: {mean}")

    return any(abs(x - mean) > THRESHOLD for x in data)
