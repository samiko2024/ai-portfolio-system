import pandas as pd
import yagmail
import schedule
import time
from app.ai_engine import generate_summary

import streamlit as st

EMAIL = st.secrets["EMAIL"]
PASSWORD = st.secrets["EMAIL_PASSWORD"]
TO = "rockwaynigeria@gmail.com"

def job():
    df = pd.read_csv("data/data.csv")
    summary = generate_summary(df.to_string())

    yag = yagmail.SMTP(EMAIL, PASSWORD)
    yag.send(
        to=TO,
        subject="📊 Daily Portfolio Report",
        contents=summary
    )

    print("Report sent!")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)