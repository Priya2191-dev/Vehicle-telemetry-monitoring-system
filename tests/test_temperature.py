from temperature import check_temperature

def test_temperature_status():
    data = [80, 105]
    result = check_temperature(data)

    assert result == ["Normal", "High"]
