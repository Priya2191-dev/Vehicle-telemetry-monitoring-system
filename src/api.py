from fastapi import FastAPI, HTTPException
from speed import monitor_speed
from typing import List

app = FastAPI()

@app.get("/speed")
def get_speed(data: List[float] = [40, 50, 60]):
    try:
        return monitor_speed(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health():
    return {"status": "running"}
