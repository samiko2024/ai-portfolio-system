import streamlit as st
import pandas as pd
from app.ai_engine import generate_summary
from app.data_manager import load_data, save_data

def show_dashboard():
    st.title("📊 Portfolio Intelligence Dashboard")

    # --- LOAD DATA ---
    df = load_data()

    # --- FILE UPLOAD ---
    uploaded_file = st.file_uploader("Upload Portfolio CSV", type=["csv"])

    if uploaded_file is not None:
        new_df = pd.read_csv(uploaded_file)

        required_cols = {"name", "kpi_progress", "capital_deployed", "risk_level"}

        if not required_cols.issubset(new_df.columns):
            st.error("CSV must contain: name, kpi_progress, capital_deployed, risk_level")
        else:
            df = new_df
            save_data(df)  # 💾 persist
            st.success("Data uploaded and saved successfully")

    # --- KPI METRICS ---
    total_capital = df["capital_deployed"].sum()
    avg_kpi = df["kpi_progress"].mean()
    high_risk_count = df[df["risk_level"] == "High"].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Capital", f"${total_capital:,.0f}")
    col2.metric("📈 Avg KPI", f"{avg_kpi:.1f}%")
    col3.metric("⚠️ High Risk", high_risk_count)

    st.divider()

    # --- CHART ---
    st.subheader("KPI Performance")
    st.bar_chart(df.set_index("name")["kpi_progress"])

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

            # --- DOWNLOAD ---
    st.download_button(
        label="Download Current Data",
        data=df.to_csv(index=False),
        file_name="portfolio_data.csv",
        mime="text/csv"
    )