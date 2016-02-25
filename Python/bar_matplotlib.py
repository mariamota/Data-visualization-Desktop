"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


# Example data

y = np.arange(1, 10)
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")

plt.show()
