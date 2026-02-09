# Model Monitoring & Drift Detection (Pure Python)

## Project Overview
This project demonstrates a **minimal ML model monitoring system** using **only built-in Python libraries** — no installations or downloads required.  

It simulates a dataset, trains a simple model, detects **data drift**, and monitors model performance — all in a single Python script.

Tools & Libraries: Python (built-in libraries, no external installations), Pandas, NumPy

##Methodology

Simulated training and test datasets with multiple features.

Trained a simple baseline model (majority class predictor) to simulate predictions.

Implemented data drift detection by comparing feature means between training and new data.

Monitored model performance; triggered alerts when accuracy dropped.

Designed the system to be fully self-contained, easily runnable from GitHub.

##Results & Impact:

Detected drift in relevant features within seconds during testing.

Identified model performance drops immediately, demonstrating proactive monitoring.

Provides a foundation for deploying real-time ML monitoring pipelines.  

## How to Run
1. Open the file [`model_monitoring_github.py`](./model_monitoring_github.py) on GitHub.  
2. Copy the code and **paste it into any Python editor or online compiler** (like [replit.com](https://replit.com) or [python.org's console](https://www.python.org/shell/)).  
3. Run the code and see the **console output** directly.

## Example OutputDrift Detection (feature mean comparison):

feature1: Train=2.58, New=2.07, Drift Detected: Yes

feature2: Train=2.31, New=2.38, Drift Detected: No

feature3: Train=2.62, New=1.88, Drift Detected: Yes

feature4: Train=2.51, New=3.04, Drift Detected: Yes

New Data Accuracy: 0.25

Model performance dropped!

##Example Output Detection Image:

<img width="602" height="226" alt="image" src="https://github.com/user-attachments/assets/670dfaae-2061-4122-a3ed-bb25e862175f" />

