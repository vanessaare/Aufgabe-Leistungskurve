import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df_activity = pd.read_csv("data/activity.csv", skipinitialspace=True)
df_activity["Time"] = df_activity.index


Leistung_Mittelwert = df_activity["PowerOriginal"].mean()
print("Die mittlere Leistung beträgt: ", Leistung_Mittelwert)

Leistung_Maximalwert = df_activity["PowerOriginal"].max()
print("Die maximale Leistung beträgt: ", Leistung_Maximalwert)


df_activity["PowerOriginal"] = df_activity["PowerOriginal"].fillna(0)
df_activity = df_activity.dropna(subset=["HeartRate"])


# Herzfrequenz-Zonen definieren

fig = go.Figure()

max_hr = 450

zones = [
    0,
    0.5 * max_hr,
    0.6 * max_hr,
    0.7 * max_hr,
    0.8 * max_hr,
    1.0 * max_hr
]

colors = [
    "rgba(0,255,0,0.05)",
    "rgba(173,255,47,0.05)",
    "rgba(255,255,0,0.05)",
    "rgba(255,165,0,0.05)",
    "rgba(255,0,0,0.05)"
]

for i in range(len(zones)-1):
    fig.add_shape(
        type="rect",
        x0=0,
        x1=df_activity["Time"].max(),
        y0=zones[i],
        y1=zones[i+1],
        fillcolor=colors[i],
        opacity=0.7,
        layer="below",
        line_width=0,
    )

labels = ["Z1", "Z2", "Z3", "Z4", "Z5"]

df_activity["Zone"] = pd.cut(df_activity["HeartRate"], bins=zones, labels=labels)

time_in_zone = df_activity["Zone"].value_counts().sort_index()
print("Zeit in Zonen (Sekunden):")
print(time_in_zone)

#fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_activity["Time"],
    y=df_activity["HeartRate"],
    mode="lines",
    name="Heart Rate"
))

fig.add_trace(go.Scatter(
    x=df_activity["Time"],
    y=df_activity["PowerOriginal"],
    mode="lines",
    name="Power"
))

fig.update_layout(
    title="Herzfrequenz & Leistung über Zeit",
    xaxis_title="Zeit (s)",
    yaxis_title="Wert"
)

fig.update_layout(
    title="Herzfrequenz & Leistung über Zeit",
    xaxis_title="Zeit (s)",
    yaxis_title="Wert",
    plot_bgcolor="white"
)
fig.update_yaxes(range=[0, df_activity["HeartRate"].max() * 1.05])

fig.show()