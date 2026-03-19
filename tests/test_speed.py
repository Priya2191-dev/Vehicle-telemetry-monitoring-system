from speed import monitor_speed

def test_monitor_speed():
    data = [40, 50, 60]
    result = monitor_speed(data)

    assert result["average"] == 50
    assert result["max"] == 60
