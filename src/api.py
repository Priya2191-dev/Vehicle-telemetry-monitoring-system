from fastapi import FastAPI
from speed import monitor_speed

app = FastAPI()

@app.get("/speed")
def get_speed():
    return monitor_speed([40, 50, 60])

@app.get("/health")
def health():
    return {"status": "running"}
