# Moody's Scenario Mock API

A **mock implementation** of the Moody's Scenario Studio API, created to simulate and visualize economic scenario data without requiring live API credentials.
Built for learning, experimentation, API integration, data processing, and visualization skills.

## **Project Overview**
- Connects to a mocked API-like interface for offline development
- Worked with endpoints and JSON responses
- Used pandas for data manipulation
- Converted raw API data into Moody's style credit ratings (short-term and long-term specific ratings)
- Mapped GDP and unemployment data to Moody's short and long term credit ratings

## **Skills Shown**
- Python 3
- Pandas (for data handling)
- Matplotlib (scrapped in favor for cleaner output)
- Mock API Design

## **How to Interpret Output**
Moody's uses a rating scale in order to categorize entity's quality in terms of investment risk:
<img width="561" height="481" alt="image" src="https://github.com/user-attachments/assets/0e32d279-0aef-4a94-9f08-3bca381d68da" />

## **How to Run Locally**
Clone the repo:
    ```bash
    git clone https://github.com/byounelijah/moodys-scenario-mock-api.git
   cd moodys-scenario-mock-api

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the script:
python3 test_s2api.py
