import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

st.set_page_config(page_title="Training Progress Tracker", layout="wide")

file_path = "progress.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=["Date", "Pushups", "Pullups", "Run_km", "Notes"])

st.sidebar.title("Menu")
selected_page = st.sidebar.selectbox("Go to", ["Log Training", "View Progress"])

if selected_page == "Log Training":
    st.title("Log Today's Training")

    pushups = st.number_input("Push-ups", min_value=0)
    pullups = st.number_input("Pull-ups", min_value=0)
    run_km = st.number_input("Running (km)", min_value=0.0, format="%.2f")
    notes = st.text_area("Notes")

    if st.button("Save Entry"):
        new_entry = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Pushups": pushups,
            "Pullups": pullups,
            "Run_km": run_km,
            "Notes": notes
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

        df.to_csv(file_path, index=False)
        st.success("Entry Saved")

elif selected_page == "View Progress":
    st.title("Progress Report")

    if not df.empty:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date", ascending=False)
        last_5 = df.head(5)

        st.subheader("Last 5 Entries")
        st.dataframe(last_5, use_container_width=True)

        fig = px.line(
            last_5.sort_values("Date"),
            x="Date",
            y=["Pushups", "Pullups", "Run_km"],
            markers=True,
            title="Performance over Last 5 Days"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("AI Feedback")
        recent = last_5.iloc[0]
        feedback = []

        if recent["Pushups"] < 100:
            feedback.append("Try to hit at least 100 push-ups a day.")
        else:
            feedback.append("They don't know you son.")

        if recent["Run_km"] < 2:
            feedback.append("Try to run at least 2 km.")
        else:
            feedback.append("Your mamas' raised a soldier")

        for line in feedback:
            st.write(line)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "training_progress.csv", "text/csv")

    else:
        st.warning("No data yet. Log your training first.")
