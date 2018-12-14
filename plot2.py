from scipy.stats import linregress as linreg
import numpy as np
import matplotlib.pyplot as plt


arrofdata = np.loadtxt('data.txt')
X = arrofdata[:, 0]
Y = arrofdata[:, 1]
arrofdata = None
a, b, r, _, da = linreg(X, Y)
a, b = a.round(), b.round()
"""
a - slope of line
b - cut off coefficient
r - correlation coefficient
p - some statistical test...
da - the error of a coefficint - standard deviation
"""

plt.figure(figsize=(16, 9))
plt.plot(X, Y, 'o', label="value y")
basex = np.linspace(min(X), max(X), 10000)
plt.plot(basex, basex * a + b, label="regression line, a = {0}, b = {1}".format(a, b))
plt.xlabel("Value $x$")
plt.ylabel("Value $y$")
plt.legend()
plt.show()
