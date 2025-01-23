"""import pandas as pd
import matplotlib.pyplot as plt

def load_analytics(file_path="analytics.csv"):
    #Load the analytics data from the CSV file.
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} records from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
        return None

def visualize_event_types(df):
    #Visualize the distribution of event types.
    event_counts = df["Type"].value_counts()
    event_counts.plot(kind="bar", title="Event Type Distribution")
    plt.xlabel("Event Type")
    plt.ylabel("Count")
    plt.show()

def visualize_screen_capture_times(df):
    #Visualize timestamps of screen captures.
    capture_times = df[df["Type"] == "screenshot"]["Timestamp"]
    capture_times = pd.to_datetime(capture_times)
    capture_times.value_counts().sort_index().plot(kind="line", title="Screenshot Capture Timeline")
    plt.xlabel("Time")
    plt.ylabel("Number of Screenshots")
    plt.show()

if __name__ == "__main__":
    analytics_data = load_analytics()
    if analytics_data is not None:
        visualize_event_types(analytics_data)
        visualize_screen_capture_times(analytics_data)"""


import streamlit as st
import pandas as pd

# Load analytics data
data = pd.read_csv("analytics.csv", names=["Timestamp", "Type", "Data1", "Data2", "Data3"])

st.title("Procrastination Prevention Analytics Dashboard")

# Display raw data
st.write("### Raw Data", data)

# Screenshot classifications
st.write("### Screenshot Classification Breakdown")
screenshot_data = data[data["Type"] == "Screenshot"]
label_counts = screenshot_data["Data2"].value_counts()
st.bar_chart(label_counts)

# Notification frequency
st.write("### Notifications Sent per Hour")
notification_data = data[data["Type"] == "Notification"]
notification_data["Timestamp"] = pd.to_datetime(notification_data["Timestamp"])
notification_data.set_index("Timestamp", inplace=True)
notification_frequency = notification_data.resample("H").size()
st.line_chart(notification_frequency)
