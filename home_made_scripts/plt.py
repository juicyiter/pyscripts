import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy import signal

data = np.loadtxt('plotdata.txt')
# left = pickle.load(open('left_y.pickle', 'rb'))
# right = pickle.load(open('right_y.pickle', 'rb'))

fig = plt.figure()
ax = fig.add_subplot(211)
bx = fig.add_subplot(212)

ax.plot(data)
pdata = np.absolute(signal.hilbert(data[:, 1]))
bx.plot(pdata)
peaks, _ = signal.find_peaks(pdata, distance=100)
bx.plot(peaks, pdata[peaks], 'x')
plt.show()
