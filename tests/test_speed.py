import pytest
from speed import monitor_speed

# Positive test cases
@pytest.mark.parametrize("data, expected_avg, expected_max", [
    ([40, 50, 60], 50.0, 60.0),
    ([10, 20, 30, 40], 25.0, 40.0),
    ([0, 100], 50.0, 100.0)
])
def test_monitor_speed_valid(data, expected_avg, expected_max):
    result = monitor_speed(data)
    assert result["average"] == expected_avg
    assert result["max"] == expected_max

# Negative test cases
def test_monitor_speed_empty():
    with pytest.raises(ValueError, match="empty"):
        monitor_speed([])

def test_monitor_speed_invalid_type():
    with pytest.raises(ValueError, match="must be a list"):
        monitor_speed("40,50,60")

def test_monitor_speed_negative_value():
    with pytest.raises(ValueError, match="negative"):
        monitor_speed([40, -10, 60])

def test_monitor_speed_non_numeric():
    with pytest.raises(ValueError, match="Invalid speed"):
        monitor_speed([40, "fast", 60])
