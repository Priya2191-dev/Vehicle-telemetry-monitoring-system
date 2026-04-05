import pytest
from temperature import check_temperature

# Positive cases
@pytest.mark.parametrize("data, expected", [
    ([80, 105], ["Normal", "High"]),
    ([100, 99], ["Normal", "Normal"]),
    ([150, 120], ["High", "High"])
])
def test_temperature_valid(data, expected):
    assert check_temperature(data) == expected

# Negative cases
def test_temperature_empty():
    with pytest.raises(ValueError):
        check_temperature([])

def test_temperature_invalid_type():
    with pytest.raises(ValueError):
        check_temperature("80,100")

def test_temperature_out_of_range():
    with pytest.raises(ValueError):
        check_temperature([300])

def test_temperature_non_numeric():
    with pytest.raises(ValueError):
        check_temperature([80, "hot"])
