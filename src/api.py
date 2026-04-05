from fastapi import FastAPI, HTTPException, Query
from typing import List
from speed import monitor_speed

app = FastAPI()

@app.get("/speed")
def get_speed(data: str = Query("40,50,60")):
    try:
        # Convert query string → list
        values = [float(x.strip()) for x in data.split(",") if x.strip()]

        if not values:
            raise ValueError("Empty data")

        return monitor_speed(values)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health():
    return {"status": "running"}
