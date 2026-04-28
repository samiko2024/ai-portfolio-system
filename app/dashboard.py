import streamlit as st
import pandas as pd
from app.ai_engine import generate_summary

def load_data():
    return pd.read_csv("data/data.csv")

def show_dashboard():
    df = load_data()

    st.title("📊 Portfolio Intelligence Dashboard")

    # --- KPI ROW ---
    total_capital = df["capital_deployed"].sum()
    avg_kpi = df["kpi_progress"].mean()
    high_risk_count = df[df["risk_level"] == "High"].shape[0]

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Capital", f"${total_capital:,.0f}")
    col2.metric("📈 Avg KPI", f"{avg_kpi:.1f}%")
    col3.metric("⚠️ High Risk", high_risk_count)

    st.divider()

    # --- CHART + TABLE ---
    col4, col5 = st.columns([2, 1])

    with col4:
        st.subheader("KPI Performance")
        st.bar_chart(df.set_index("name")["kpi_progress"])

    with col5:
        st.subheader("Risk Breakdown")
        st.write(df["risk_level"].value_counts())

    st.divider()

    # --- TABLE ---
    st.subheader("Portfolio Data")

    def highlight_risk(row):
        if row["risk_level"] == "High":
            return ["background-color: #ff4b4b"] * len(row)
        return [""] * len(row)

    st.dataframe(df.style.apply(highlight_risk, axis=1))

    st.divider()

    st.subheader("🤖 AI Summary")
    if st.button("Generate AI Report"):
        summary = generate_summary(df.to_string())

        if "⚠️" in summary:
            st.warning("AI unavailable — showing basic insights instead")

            # fallback logic
            avg_kpi = df["kpi_progress"].mean()
            high_risk = df[df["risk_level"] == "High"].shape[0]

            st.write(f"""
            Basic Report:
            - Average KPI: {avg_kpi}
            - High Risk Projects: {high_risk}
            """)

        else:
            st.write(summary)