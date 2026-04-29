import pandas as pd
import os

DATA_PATH = "data/data.csv"

def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame(columns=["name", "kpi_progress", "capital_deployed", "risk_level"])

def save_data(df):
    df.to_csv(DATA_PATH, index=False)