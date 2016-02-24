"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


# Example data

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")

plt.show()
