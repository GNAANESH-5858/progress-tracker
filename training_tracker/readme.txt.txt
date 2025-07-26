TRAINING PROGRESS TRACKER APP

Description:
A personal training progress tracker built using Python and Streamlit.
Log your daily push-ups, pull-ups, and running distance. View reports and graphs of your weekly progress.


Folder Contents:

app.py                - Main app file
progress.csv          - (Optional) Saved workout data
launch.bat            - Click to start the app (shows terminal)
launch.vbs            - Click to start the app silently (no terminal)

 Requirements:
- Python 3.10+ installed
- Pip installed
- Streamlit and Plotly libraries

Install dependencies with:
> pip install streamlit plotly pandas


How to Run:
Option 1: Manual
> Open CMD or Terminal
> Navigate to the folder:
  cd Desktop\training_tracker
> Run:
  streamlit run app.py

Option 2: Auto-start
> Just double-click:
  - launch.bat (shows terminal)
  - launch.vbs (hides terminal)



- Data is stored using Pandas in a local CSV file.
- Graphs are created using Plotly for visual progress tracking.
- The app layout is built using Streamlit with two pages:
    1. Log Today's Training
    2. Progress Report
- Built and understood completely from scratch within a week.


Made by: Gnaanesh .K
Second Year CSE – CS Club
