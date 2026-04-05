import pytest
from brake import brake_analysis

# Positive Test Cases
@pytest.mark.parametrize("data, expected", [
    ([10, 20], [2.0, 4.0]),
    ([5, 15], [1.0, 3.0]),
    ([0, 50], [0.0, 10.0])
])
def test_brake_analysis_valid(data, expected):
    assert brake_analysis(data) == expected

# Negative Test Cases
def test_brake_analysis_empty():
    with pytest.raises(ValueError, match="empty"):
        brake_analysis([])

def test_brake_analysis_invalid_type():
    with pytest.raises(ValueError, match="must be a list"):
        brake_analysis("10,20")

def test_brake_analysis_negative_values():
    with pytest.raises(ValueError, match="negative"):
        brake_analysis([10, -5])

def test_brake_analysis_non_numeric():
    with pytest.raises(ValueError, match="Invalid value"):
        brake_analysis([10, "abc"])
