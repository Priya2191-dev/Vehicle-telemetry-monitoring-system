# 🚗 Vehicle Telemetry Monitoring System

## Objective

A comprehensive Python-based automation framework for monitoring and testing vehicle telemetry data including speed, temperature, braking, anomaly detection, telemetry visualisation, FastAPI. 

## Overview

This project simulates, validates, analyzes, and visualizes vehicle telemetry data for automotive systems. It also exposes telemetry insights through APIs and ensures quality using automation testing.

## Features

- Speed Monitoring:

  Calculates average and maximum speed.

  Handles invalid inputs.
  
- Engine Temperature Monitoring:

  Detects overheating conditions.
  
- Brake Pressure Analysis:

  Computes braking force logic.
  
- Telemetry Visualization:

  Visualise telemetry data like speed and pressure to understand system behaviour.
  
- AI-Based Anomaly Detection:

  Detects abnormal data using statistical logic.
  
- REST API using FastAPI:

  Exposes telemetry data via REST API, allows integration with external system, supports real time  data access, built using light    weight FastAPI framework.
  
## Installations

git clone https://github.com/Priya2191-dev/Vehicle-telemetry-monitoring-system.git

cd Vehicle-telemetry-monitoring-system

pip install -r requirements.txt

## Tech Stack

- Language: Python
- Testing: Pytest, Behave(BDD)
- CI/CD: Github Actions
- Visualisation: Matplotlib
- Data Analysis: NumPy
- API Layer: FastAPI
- Reporting: Allure Reports

## Testing Strategy

- Unit Testing using Pytest
- Behavior-Driven Testing using Behave
- Edge Case Handling
- Input Validation Testing
- Negative Scenario Testing

## CI/CD Pipeline

- Runs on every push & pull request.
- Executes:

  Pytest(Unit tests)

  Behave(BDD tests)

- Generates:

  Allure reports

  Coverage reports

  Dashboard plots

## Reports & Outputs

- Allure Test Reports
- Behave Execution Logs
- Coverage Report
- Dashboard Plot(plot.png)

## Conclusion

Successfully tested Python-based telemetry monitoring and validation framework that simulates real world vehicle data processing, testing, and API exposure using modern automation practices.

## Author

Priyanka Lale 

