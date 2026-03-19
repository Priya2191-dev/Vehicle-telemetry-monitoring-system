def check_temperature(data):
    return ["High" if t > 100 else "Normal" for t in data]
