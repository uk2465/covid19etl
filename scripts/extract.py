# scripts/extract.py
import requests
import pandas as pd
import json
from datetime import datetime

def extract_covid_data():
    url = "https://corona.lmao.ninja/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()
    
    # Save raw data with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"raw_data/covid_data_{timestamp}.json", "w") as f:
        json.dump(data, f)
    
    return data
