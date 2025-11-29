import matplotlib.pyplot as plt

# Define the coordinates of the points
x_coordinates = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
]
y_coordinates = [
    0.857,
    0.960,
    0.999,
    0.972,
    0.877,
    0.710,
    0.474,
    0.176,
    -0.161,
    -0.504,
    -0.797,
    -0.974,
    -0.759,
    -0.348,
    0.175,
    0.666,
    0.963,
    0.950,
    0.614,
    0.064,
    -0.508,
    -0.902,
    -0.990,
    -0.765,
    -0.318,
    0.198,
    0.643,
    0.920,
    0.999,
    0.898,
    0.667,
    0.364,
    0.041,
    -0.264,
    -0.528,
    -0.738,
]

# Plot the points with circle markers
# linestyle='' to prevent connecting lines
plt.plot(x_coordinates, y_coordinates, marker="o", linestyle="--")

# Add labels and a title
plt.xlabel("sample index")
plt.ylabel("amplitude")
plt.title("Phase Modulation Plot")

# Display the plot
plt.show()
