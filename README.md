# Vehicle-telemetry-monitoring-system
Python based vehicle telemetry monitoring system that simulates and analyses real time vehicle data  and test it using pytest and BDD test

# ๐— Vehicle Telemetry Monitoring System

A Python-based simulation and automation framework for monitoring vehicle telemetry data such as **speed, engine temperature, and brake pressure**, enriched with **data visualization, AI anomaly detection, and REST APIs**.

This project demonstrates how modern automotive systems can be designed, tested, and validated using **automation testing, BDD, and CI/CD pipelines**.

---

## ๐“ Overview

The system simulates real-time telemetry data from a vehicle and processes it through multiple modules:

- Monitoring and analysis of vehicle parameters
- Visualization of telemetry data
- Detection of anomalies using statistical logic
- Exposure of data via REST APIs
- Automated testing using Pytest and BDD

---

## ๐งฉ Features

### ๐ 1. Speed Monitoring
- Calculates average and maximum speed
- Helps evaluate vehicle performance
- Provides input for anomaly detection

---

### ๐ก๏ธ 2. Engine Temperature Tracking
- Monitors engine temperature values
- Detects overheating conditions
- Supports predictive maintenance

---

### ๐‘ 3. Brake Pressure Analysis
- Analyzes braking force applied
- Simulates braking impact on speed
- Ensures safe braking behavior

---

### ๐“ 4. Telemetry Visualization
- Plots speed and pressure data
- Generates graphical insights
- Saves output as image for reporting

---

### ๐ค– 5. AI-Based Anomaly Detection
- Detects abnormal values using statistical deviation
- Identifies unsafe conditions
- Can be extended to ML-based models

---

### ๐ 6. REST API (FastAPI)
- Exposes telemetry data via APIs
- Enables integration with external systems
- Lightweight and high-performance

---

## ๐—๏ธ System Architecture

```mermaid
graph TD

A[Input Data] --> B[Speed Monitoring]
A --> C[Temperature Tracking]
A --> D[Brake Analysis]

B --> E[Telemetry Processing]
C --> E
D --> E

E --> F[Anomaly Detection]
E --> G[Visualization]

E --> H[FastAPI Service]
H --> I[External Systems]
```

---

## ๐“ Dashboard Visualization

The system generates telemetry plots such as:

- Speed trends
- Brake pressure trends

### ๐”น Example Output

> Add your generated image inside `images/plot.png`

![Telemetry Plot](images/plot.png)

---

## ๐“ Project Structure

```
vehicle-telemetry-monitoring/
โ”
โ”โ”€โ”€ src/
โ” โ”โ”€โ”€ speed.py
โ” โ”โ”€โ”€ temperature.py
โ” โ”โ”€โ”€ brake.py
โ” โ”โ”€โ”€ telemetry.py
โ” โ”โ”€โ”€ anomaly.py
โ” โ””โ”€โ”€ api.py
โ”
โ”โ”€โ”€ tests/ # Pytest tests
โ”โ”€โ”€ features/ # BDD tests
โ” โ””โ”€โ”€ steps/
โ”
โ”โ”€โ”€ images/ # Output plots
โ” โ””โ”€โ”€ plot.png
โ”
โ”โ”€โ”€ requirements.txt
โ”โ”€โ”€ README.md
โ””โ”€โ”€ .github/workflows/ # CI/CD pipeline
```

---

## โ๏ธ Installation

### ๐”น 1. Clone Repository

```
git clone https://github.com/your-username/vehicle-telemetry-monitoring.git
cd vehicle-telemetry-monitoring
```

---

### ๐”น 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## โ–ถ๏ธ Running the Project

### ๐”น Run API Server

```
uvicorn src.api:app --reload
```

Access endpoints:
- http://127.0.0.1:8000/speed
- http://127.0.0.1:8000/health

---

### ๐”น Run Pytest

```
pytest -v
```

---

### ๐”น Run BDD Tests

```
behave
```

---

## ๐งช Testing Strategy

### โ… Unit Testing (Pytest)
- Validates individual modules
- Ensures correctness of logic

### โ… BDD Testing (Behave)
- Scenario-based validation
- Human-readable test cases

---

## ๐” CI/CD Pipeline

The project uses GitHub Actions to:
- Automatically run tests on every push
- Validate code quality
- Ensure build stability

---

## ๐““ Google Colab Support

You can run this project in Google Colab:

1. Upload files
2. Install dependencies
3. Execute modules interactively

---

## ๐ง  Learning Outcomes

This project helps you understand:

- Automotive telemetry systems
- Automation testing (Pytest + BDD)
- API development using FastAPI
- Data visualization
- AI anomaly detection basics
- CI/CD implementation

---

## ๐€ Future Enhancements

- Real-time dashboard (Streamlit/Dash)
- Machine learning-based anomaly detection
- Cloud deployment
- Integration with real vehicle data

---

## ๐ค Contribution

Contributions are welcome!

- Add new features
- Improve test coverage
- Optimize performance

---

## ๐“ License

This project is open-source under the MIT License.

---

## โญ Support

If you like this project:
- โญ Star the repository
- ๐ด Fork it
- ๐”— Share it

---

## ๐ฏ Conclusion

This project demonstrates how modern vehicle telemetry systems can be simulated, monitored, and validated using automation frameworks. By combining real-time data processing, visualization, anomaly detection, and API integration, it provides a strong foundation for building intelligent and scalable automotive monitoring solutions.
