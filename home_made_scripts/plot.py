import pickle
import numpy as np
import matplotlib.pyplot as plt


data = pickle.load(open('out.pickle', 'rb'))

first = np.zeros(1)
second = np.zeros(1)
i = 0
while i <= (len(data) // 960):
    first = np.append(first, data[i * 960: (i + 1) * 960])
    first = np.append(first, np.ones(1) * ((i + 1) % 2))
    second = np.append(second, data[(i + 1) * 960: (i + 2) * 960])
    second = np.append(second, np.zeros(1))
    i += 2

if len(first) > len(second):
    first = first[:len(second)]

first = np.reshape(first, (len(first), 1))
second = np.reshape(second, (len(second), 1))
plt.plot(np.append(first, second, axis=1))
plt.show()
