import pytest
from anomaly import detect_anomaly


def test_detect_anomaly_true():
    assert detect_anomaly([50, 55, 120]) is True

def test_detect_anomaly_false():
    assert detect_anomaly([50, 52, 55]) is False

def test_empty_input():
    with pytest.raises(ValueError):
        detect_anomaly([])

def test_invalid_input():
    with pytest.raises(ValueError):
        detect_anomaly([50, "high", 60])
