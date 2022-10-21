#plot some points
import random

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

x=[45.998,
616.374,
2869.371,
8680.429]

y=[198.01,
2533.983,
12189.218,47720.39]

coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients
r2_error=r2_score(y, poly1d_fn(x))
plt.tight_layout()
plt.title('"kill" vs "do-nothing" border\nat 50% starting occupancy')
plt.xlabel('Number of iterations with "kill" border')
plt.ylabel('Number of iterations with "do-nothing" border')
plt.plot(x, y, 'ro', x, poly1d_fn(x), '-b')
plt.errorbar(x, poly1d_fn(x), yerr=poly1d_fn(x) - y, fmt='.k')
#add the r2 error

plt.text(1000, 40000, r'$R^2$ error: %s' % round(r2_error,2), fontsize=13)

#write the equation
plt.text(1000, 35000, r'$y=%s*x+%s$' % (round(coef[0],2),round(coef[1],2)), fontsize=13)

#above the first pont write 5x5
plt.text(-200, 2000, '5x5', fontsize=13)

#above the second pont write 10x10
plt.text(616.374, 0, '10x10', fontsize=13)

#above the third pont write 15x15
plt.text(3000, 12189.218, '15x15', fontsize=13)

#above the fourth pont write 20x20
plt.text(7500, 47720.39, '20x20', fontsize=13)

plt.savefig('plot.png', dpi=600)