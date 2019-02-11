import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('plotdata.txt')

plt.plot(data[::3])
plt.show()
