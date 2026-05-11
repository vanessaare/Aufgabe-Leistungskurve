from pathlib import Path

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from load_data import load_data
from sort import bubble_sort


def main():
    
    # Daten laden
    data = load_data("activity.csv")

    # Spaltenname
    power_values = data["PowerOriginal"].tolist()

    # Sortieren
    sorted_power = bubble_sort(power_values)

    # x-Achse
    x_values = range(len(sorted_power))

    # Plot erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, sorted_power)

    plt.xlabel("Zeitpunkte")
    plt.ylabel("Leistung [W]")
    plt.title("Power Curve")
    plt.grid(True)

    # Ordner erstellen
    figures_path = Path("figures")
    figures_path.mkdir(exist_ok=True)

    # Speichern
    plt.savefig(figures_path / "power_curve.png")

    # Anzeigen
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()