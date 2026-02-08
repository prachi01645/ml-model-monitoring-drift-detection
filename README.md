# Model Monitoring & Drift Detection (Pure Python)

## Project Overview
This project demonstrates a **minimal ML model monitoring system** using **only built-in Python libraries** — no installations or downloads required.  

It simulates a dataset, trains a simple model, detects **data drift**, and monitors model performance — all in a single Python script.

## Features
- Simulates training and test datasets with multiple features  
- Trains a simple baseline model (majority class predictor)  
- Detects **data drift** by comparing feature means  
- Monitors model performance and alerts if performance drops  
- Fully **self-contained**: can be viewed and run directly from GitHub  

## How to Run
1. Open the file [`model_monitoring_github.py`](./model_monitoring_github.py) on GitHub.  
2. Copy the code and **paste it into any Python editor or online compiler** (like [replit.com](https://replit.com) or [python.org's console](https://www.python.org/shell/)).  
3. Run the code and see the **console output** directly.

## Example OutputDrift Detection (feature mean comparison):

feature1: Train=2.48, New=2.95, Drift Detected: Yes

feature2: Train=1.76, New=1.82, Drift Detected: No

feature3: Train=2.50, New=2.80, Drift Detected: Yes

feature4: Train=2.41, New=2.70, Drift Detected: Yes

New Data Accuracy: 0.62
Model performance is stable.
