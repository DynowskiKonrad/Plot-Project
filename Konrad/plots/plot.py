import numpy as np # crucial for matplotlib
import matplotlib.pyplot as plt # used for plotting

x = np.linspace(-2, 2, 500)
y1 = np.sin(np.pi*x) #easy way, calculates for all points (smaller number, highest number, number of points)
y2 = np.cos(np.pi*x)

plt.figure(figsize=(4, 3))

plt.plot(x, y1, "+", label="sine")
plt.plot(x, y2, "o", label="cosine")
plt.xlabel("Argument $x$")
plt.ylabel("Value $y$")

leg = plt.legend()
leg.draggable()

plt.tight_layout(0.1)

plt.show()

"""
np.loadtxt
using this method load text data for your program
"""