import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def brake_analysis(data: List[float]) -> List[float]:
    """
    Analyze brake pressure data by applying scaling factor.

    Args:
        data (List[float]): List of brake pressure values

    Returns:
        List[float]: Scaled brake pressure values

    Raises:
        ValueError: If input is invalid
    """

    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    if not data:
        raise ValueError("Input list cannot be empty")

    result = []

    for p in data:
        if not isinstance(p, (int, float)):
            raise ValueError(f"Invalid value in data: {p}")

        if p < 0:
            raise ValueError(f"Brake pressure cannot be negative: {p}")

        scaled = round(p * 0.2, 2)
        result.append(scaled)

    logging.info(f"Input: {data} | Output: {result}")
    return result
