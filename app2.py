import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import numpy as np
from matplotlib.lines import Line2D

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("shots2.csv")

# Create team label
df['team'] = df['team_home'].apply(lambda x: 'Italy' if x else 'Northern Ireland')

# -----------------------------
# TITLE
# -----------------------------
st.title("⚽ Italy vs Northern Ireland - Shot Analysis Dashboard")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

team_filter = st.sidebar.selectbox("Select Team", ["All", "Italy", "Northern Ireland"])
shot_filter = st.sidebar.selectbox("Shot Type", ["All"] + list(df['shot_type'].unique()))

# Apply filters
filtered_df = df.copy()

if team_filter != "All":
    filtered_df = filtered_df[filtered_df['team'] == team_filter]

if shot_filter != "All":
    filtered_df = filtered_df[filtered_df['shot_type'] == shot_filter]

# -----------------------------
# 1. KEY METRICS
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

total_shots = len(filtered_df)
goals = len(filtered_df[filtered_df['shot_type'] == 'goal'])
on_target = len(filtered_df[filtered_df['shot_type'].isin(['goal', 'save'])])

col1.metric("Total Shots", total_shots)
col2.metric("Goals", goals)
col3.metric("On Target", on_target)

# -----------------------------
# 2. DATA TABLE
# -----------------------------
st.subheader("📋 Shot Data")
st.dataframe(filtered_df)

# -----------------------------
# 3. SHOT MAP (NO SCALING ✅)
# -----------------------------
st.subheader("📍 Shot Map (With Distance)")

pitch = Pitch(
    pitch_type='statsbomb',
    pitch_color='#dbe2b0',
    line_color='white'
)

fig, ax = pitch.draw(figsize=(10, 6))

plot_df = filtered_df.copy()

# ✅ ONLY flip Northern Ireland (NO scaling)
if team_filter == "Northern Ireland":
    plot_df['x'] = 120 - plot_df['x']
    plot_df['y'] = 80 - plot_df['y']

# Distance to goal
plot_df['distance'] = np.sqrt(
    (120 - plot_df['x'])**2 + (40 - plot_df['y'])**2
).round(1)

# Colors
shot_colors = {
    "goal": "green",
    "miss": "red",
    "block": "orange",
    "save": "purple",
    "post": "blue"
}

# Plot shots
for _, row in plot_df.iterrows():
    ax.scatter(
        row['x'], row['y'],
        color=shot_colors.get(row['shot_type'], "black"),
        s=140,
        edgecolors='black',
        alpha=0.9
    )

    # Distance label
    ax.text(
        row['x'] + 1,
        row['y'] + 1,
        f"{row['distance']}m",
        fontsize=8,
        color='black'
    )

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Goal', markerfacecolor='green', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Miss', markerfacecolor='red', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Block', markerfacecolor='orange', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Post', markerfacecolor='blue', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Save', markerfacecolor='purple', markeredgecolor='black')
]

ax.legend(handles=legend_elements, title="Shot Outcome", loc="upper right")
ax.set_title("Shot Map with Distance to Goal")

st.pyplot(fig)

# -----------------------------
# 4. PLAYER ANALYSIS
# -----------------------------
st.subheader("👤 Player Shots")

player_shots = filtered_df['player'].value_counts().reset_index()
player_shots.columns = ['Player', 'Shots']

st.dataframe(player_shots)

# -----------------------------
# 5. SHOT SITUATIONS
# -----------------------------
st.subheader("⚙️ Shot Situations")

if 'situation' in filtered_df.columns:
    situation_counts = filtered_df['situation'].value_counts()
    st.bar_chart(situation_counts)
else:
    st.info("No 'situation' column found in dataset")

# -----------------------------
# 6. KEY INSIGHTS (DYNAMIC)
# -----------------------------
st.subheader("🧠 Key Insights")

if total_shots > 0:
    conversion = (goals / total_shots) * 100

    st.markdown(f"""
- The team produced **{total_shots} shots** with a conversion rate of **{conversion:.1f}%**
- **{on_target} shots on target** indicate finishing efficiency levels
""")

    if conversion < 10:
        st.markdown("- ⚠️ Low conversion rate suggests poor shot quality or finishing")

    blocks = len(filtered_df[filtered_df['shot_type'] == 'block'])
    if blocks > 0:
        st.markdown(f"- 🧱 {blocks} shots were blocked, indicating defensive pressure")

    misses = len(filtered_df[filtered_df['shot_type'] == 'miss'])
    if misses > goals:
        st.markdown("- 🎯 High number of misses suggests suboptimal shot selection")

else:
    st.warning("No data available for selected filters")