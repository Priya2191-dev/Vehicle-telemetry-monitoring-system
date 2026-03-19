from brake import brake_analysis

def test_brake_analysis():
    data = [10, 20]
    result = brake_analysis(data)

    assert result == [2.0, 4.0]
