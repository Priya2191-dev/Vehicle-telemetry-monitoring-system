# 🚗 Vehicle Telemetry Monitoring System

A comprehensive Python-based automation framework for monitoring and testing vehicle telemetry data including speed, temperature, braking, and anomaly detection.

## Overview

This project simulates, validates, analyzes, and visualizes vehicle telemetry data for automotive systems. It also exposes telemetry insights through APIs and ensures quality using automation testing.

## Features

- Speed Monitoring
- Engine Temperature Tracking
- Brake Pressure Analysis
- Telemetry Visualization
- AI-Based Anomaly Detection
- REST API using FastAPI
  
## Installation

git clone https://github.com/Priya2191-dev/Vehicle-telemetry-monitoring-system.git

cd Vehicle-telemetry-monitoring-system

pip install -r requirements.txt

## Interactive Simulation Demo

Run the vehicle telemetry monitoring system :

[Open in Google Colab] (https://colab.research.google.com/github/Priya2191-dev/Vehicle-telemetry-monitoring-system/blob/main/notebook/Vehicle-telemetry-monitoring-system.ipynb)

## Tests

- Automation Testing (Pytest + BDD)
- CI/CD Integration

## Usage

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

