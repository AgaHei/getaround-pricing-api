import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/cleaned_getaround_data.csv")

# Title
st.title("🚗 Getaround Delay Conflict Dashboard")
st.markdown("""
This dashboard helps the Product Manager evaluate how late returns affect future rentals.
Use the controls below to simulate different delay thresholds and scopes. For clarity, only rentals with a delay at checkout between 0 and 600 minuets are considered.""")

# Threshold slider
threshold = st.slider("Select delay threshold (minutes)", 15, 600, 60, step=15)

# Scope selector
scope = st.radio("Apply to:", ["All cars", "Connect cars only"])

# Filter by scope
if scope == "Connect cars only":
    df = df[df["checkin_type"] == "connect"]

# Conflict simulation
conflicts = df[
    (df["time_delta_with_previous_rental_in_minutes"].notnull()) &
    (df["delay_at_checkout_in_minutes"] > df["time_delta_with_previous_rental_in_minutes"]) &
    (df["time_delta_with_previous_rental_in_minutes"] < threshold)
]

# Display results
st.metric("Number of rentals affected", len(conflicts))

# Plot delay distribution
st.subheader("Delay Distribution (Zoomed ≤ 600 min)")
filtered_df = df[df["delay_at_checkout_in_minutes"] <= 600]
fig, ax = plt.subplots()
ax.hist(filtered_df["delay_at_checkout_in_minutes"], bins=50, color="skyblue", edgecolor="black", alpha=0.6, density=True)
sns.kdeplot(filtered_df["delay_at_checkout_in_minutes"], ax=ax, color="tomato", linewidth=2)
ax.set_title("Late Checkout Distribution")
ax.set_xlabel("Delay at Checkout (minutes)")
ax.set_ylabel("Density")
ax.set_xlim(0, 600)
st.pyplot(fig)

# Simulate conflicts across thresholds
thresholds = np.arange(15, 601, 15)
conflict_counts = []

for t in thresholds:
    conflicts = df[
        (df["time_delta_with_previous_rental_in_minutes"].notnull()) &
        (df["delay_at_checkout_in_minutes"] > df["time_delta_with_previous_rental_in_minutes"]) &
        (df["time_delta_with_previous_rental_in_minutes"] < t)
    ]
    conflict_counts.append(len(conflicts))

# Plot
st.subheader("📈 Conflicts by Delay Threshold")
fig1, ax1 = plt.subplots()
ax1.plot(thresholds, conflict_counts, marker='o', color='tomato')
ax1.set_xlabel("Delay Threshold (minutes)")
ax1.set_ylabel("Number of Conflicts")
ax1.set_title("Impact of Delay Threshold on Rental Conflicts")
ax1.grid(True)
st.pyplot(fig1)

# Calculate late return rates
connect_df = df[df["checkin_type"] == "connect"]
mobile_df = df[df["checkin_type"] != "connect"]

connect_late_pct = (connect_df["delay_at_checkout_in_minutes"] > 0).mean() * 100
mobile_late_pct = (mobile_df["delay_at_checkout_in_minutes"] > 0).mean() * 100

# Plot
st.subheader("📊 Late Return Rate by Check-in Type")
fig2, ax2 = plt.subplots()
ax2.bar(["Connect", "Mobile"], [connect_late_pct, mobile_late_pct], color=["steelblue", "orange"])
ax2.set_ylabel("Late Return Rate (%)")
ax2.set_title("Late Returns by Check-in Type")
ax2.grid(True)
st.pyplot(fig2)
st.markdown(f"""
- **Connect Cars Late Return Rate:** {connect_late_pct:.2f}%
- **Mobile Cars Late Return Rate:** {mobile_late_pct:.2f}%
""")


