import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

def monitor_speed(data: List[float]) -> Dict[str, float]:
    """
    Monitor vehicle speed and return statistics.

    Args:
        data (List[float]): List of speed values

    Returns:
        Dict[str, float]: Contains average and max speed

    Raises:
        ValueError: If input is invalid
    """

    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    if not data:
        raise ValueError("Speed data cannot be empty")

    validated_data = []

    for speed in data:
        if not isinstance(speed, (int, float)):
            raise ValueError(f"Invalid speed value: {speed}")

        if speed < 0:
            raise ValueError(f"Speed cannot be negative: {speed}")

        validated_data.append(float(speed))

    avg_speed = round(sum(validated_data) / len(validated_data), 2)
    max_speed = max(validated_data)

    result = {
        "average": avg_speed,
        "max": max_speed
    }

    logging.info(f"Input: {validated_data} | Output: {result}")
    return result
