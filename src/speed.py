def monitor_speed(data):
    return {
        "average": sum(data)/len(data),
        "max": max(data)
    }
