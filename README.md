# 🚗 Vehicle Telemetry Monitoring System

A comprehensive Python-based automation framework for monitoring and testing vehicle telemetry data including speed, temperature, braking, and anomaly detection.

## Overview

This project simulates, validates, analyzes, and visualizes vehicle telemetry data for automotive systems. It also exposes telemetry insights through APIs and ensures quality using automation testing.

## Features

- Speed Monitoring:

  It monitors vehicle speed in real time.
  
- Engine Temperature Tracking:

  Tracks engine temperature to prevent overheating.
  
- Brake Pressure Analysis:

  Analyze brake force applied to vehicle.
  
- Telemetry Visualization:

  Visualise telemetry data like speed and pressure to understand system behaviour.
  
- AI-Based Anomaly Detection:

  Detects abnormal pattern in telemetry data.
  
- REST API using FastAPI:

  Exposes telemetry data via REST API, allows integration with external system, supports real time data access, built using light    weight FastAPI framework.
  
## Installations

git clone https://github.com/Priya2191-dev/Vehicle-telemetry-monitoring-system.git

cd Vehicle-telemetry-monitoring-system

pip install -r requirements.txt

## Interactive Simulation Demo

Run the vehicle telemetry monitoring system :

[Open in Google Colab] (https://colab.research.google.com/github/Priya2191-dev/Vehicle-telemetry-monitoring-system/blob/main/notebook/Vehicle-telemetry-monitoring-system.ipynb)

## Testing

- Automation Testing (Pytest + BDD)
- CI/CD Integration

## Usages

Run tests:

- pytest
- behave

Run API:

uvicorn src.api:app --reload

## CI/CD

GitHub Actions pipeline runs pytest and behave automatically on every push and pull request.

## Technologies

- FastAPI
- NumPy
- Matplotlib
- Pytest
- Behave

## Author

Priyanka Lale 

