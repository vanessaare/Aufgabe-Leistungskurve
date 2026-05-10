def bubble_sort(data):
    sorted_data = data.copy()
    n = len(sorted_data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_data[j] < sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = (
                    sorted_data[j + 1],
                    sorted_data[j],
                )

    print(sorted_data)
    return sorted_data