import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df_activity = pd.read_csv("activity.csv", skipinitialspace=True)

#print(df_activity.tail())
#print(df_activity.info())      # Struktur
#print(df_activity.describe())  # Statistik

Leistung_Mittelwert = df_activity["PowerOriginal"].mean()
print(Leistung_Mittelwert)