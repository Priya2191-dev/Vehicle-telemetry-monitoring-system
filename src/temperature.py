import logging
from typing import List

logging.basicConfig(level=logging.INFO)

THRESHOLD = 100  

def check_temperature(data: List[float]) -> List[str]:
    """
    Classify engine temperature as 'High' or 'Normal'.

    Args:
        data (List[float]): Temperature readings

    Returns:
        List[str]: Status list
    """

    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    if not data:
        raise ValueError("Temperature data cannot be empty")

    result = []

    for t in data:
        if not isinstance(t, (int, float)):
            raise ValueError(f"Invalid temperature value: {t}")

        if t < -50 or t > 200:  # realistic bounds
            raise ValueError(f"Out-of-range temperature: {t}")

        status = "High" if t > THRESHOLD else "Normal"
        result.append(status)

    logging.info(f"Input: {data} | Output: {result}")
    return result
