import numpy as np

def detect_anomaly(data):
    mean = np.mean(data)
    return any(abs(x - mean) > 30 for x in data)
