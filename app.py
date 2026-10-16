
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Integrated Multi-Indicator Dashboard",
    layout="wide"
)

st.title("🌍 Integrated Multi-Indicator Dashboard")
st.write("Rural Sustainability Research Platform")

# Example data (not real research data)
data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025] * 2,
    "Country": ["Japan"] * 6 + ["China"] * 6,
    "Agriculture": [60, 63, 65, 68, 70, 74,
                    55, 58, 62, 66, 69, 72],
    "Tourism": [45, 48, 55, 65, 72, 78,
                40, 46, 53, 60, 68, 75],
    "Environment": [70, 72, 75, 77, 80, 83,
                    65, 67, 70, 73, 76, 79]
}

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Data Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["Japan", "China"]
)

indicator = st.sidebar.selectbox(
    "Select Indicator",
    ["Agriculture", "Tourism", "Environment"]
)

year_range = st.sidebar.slider(
    "Select Year Range",
    2020, 2025, (2020, 2025)
)

# Filter data
filtered = df[
    (df["Country"] == country) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

# Display chart
st.subheader(f"{indicator} Trends in {country}")

st.line_chart(
    filtered.set_index("Year")[indicator]
)

# Display table
st.subheader("Data Table")
st.dataframe(filtered, hide_index=True)

st.caption("All data shown are illustrative, not official statistics.")
