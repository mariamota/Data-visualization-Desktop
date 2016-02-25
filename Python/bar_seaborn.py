import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", context="talk")

# Set up the matplotlib figure
f, (ax1) = plt.subplots()

# Generate some sequential data
#x = np.array(list("012345678"))

y= np.arange(1, 10)
N = len(y)
x = range(N)
sns.barplot(x, y, palette="BuGn_d")
ax1.set_ylabel("Sequential")


plt.show()