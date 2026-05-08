import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubble_sort

def power_curve_Meli():
    # Load the data
    data = load_data()
    
    # Sort the data
    sorted_data = bubble_sort(data)
    
    # Create the power curve
    plt.plot(sorted_data, marker='o')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Power Output (kW)')
    plt.title('Power Curve for Meli Turbine')
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    power_curve_Meli()

    