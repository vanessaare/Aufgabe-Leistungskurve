import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df_activity = pd.read_csv("activity.csv", skipinitialspace=True, usecols=["Duration", "HeartRate", "PowerOriginal"])
df_activity = df_activity.dropna(subset=["HeartRate", "PowerOriginal"])  # Entfernen von Zeilen mit fehlenden Werten
#print(df_activity.tail())
#print(df_activity.info())      # Struktur
#print(df_activity.describe())  # Statistik

Leistung_Mittelwert = df_activity["PowerOriginal"].mean()
print("Die mittlere Leistung beträgt: ", Leistung_Mittelwert)

Leistung_Maximalwert = df_activity["PowerOriginal"].max()
print("Die maximale Leistung beträgt: ", Leistung_Maximalwert)



# Zeitachse bauen (jede Zeile = 1 Sekunde)
df_activity["Duration"] = df_activity.index

fig = go.Figure()

# Herzfrequenz
fig.add_trace(go.Scatter(
    x=df_activity["Duration"],
    y=df_activity["HeartRate"],
    mode="lines",
    name="Heart Rate"
))

# Leistung (Power)
fig.add_trace(go.Scatter(
    x=df_activity["Duration"],
    y=df_activity["PowerOriginal"],
    mode="lines",
    name="Power"
))

fig.update_layout(
    title="Herzfrequenz & Leistung über Zeit",
    xaxis_title="Zeit in ms",
    yaxis_title="Messwerte in mV"
)


fig.show()

df_activity