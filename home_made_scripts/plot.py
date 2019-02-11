import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
data = np.loadtxt('test.txt')
t = np.linspace(1, 20, 20*48)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5*fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
for i in range(len(data)):
    for j in range(len(data[i])):
        if np.absolute(data[i][j]) > 1:
            data[i][j] = 0
##print(data)
y = butter_bandpass_filter(data, 16, 23, 48)
fig = plt.figure(1)
ax = fig.add_subplot(111)
lines = ax.plot(y[960:2*960])
ax.legend(['channel {}'.format(c) for c in [0, 1, 2, 3]],
          loc='lower left', ncol=4,
          bbox_to_anchor=(0., 1.02, 1., .102))
plt.show()
