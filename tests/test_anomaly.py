from anomaly import detect_anomaly

def test_detect_anomaly_true():
    data = [50, 55, 120]   # anomaly present
    assert detect_anomaly(data) == True

def test_detect_anomaly_false():
    data = [50, 52, 55]   # normal
    assert detect_anomaly(data) == False
