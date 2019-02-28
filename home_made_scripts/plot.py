import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

ch_num = 3
raw_data = np.genfromtxt('output.txt')
print(len(raw_data))
raw_data = np.append(raw_data, np.zeros(ch_num - len(raw_data) % ch_num))
print(len(raw_data))
data = raw_data.reshape(-1, ch_num)
# t = np.linspace(1, 20, 20*48)

# def butter_bandpass(lowcut, highcut, fs, order=5):
#     nyq = 0.5*fs
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter(order, [low, high], btype='band')
#     return b, a

# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         if np.absolute(data[i][j]) > 1:
#             data[i][j] = 0
# ##print(data)
# y = butter_bandpass_filter(data, 16, 23, 48)
fig = plt.figure(1)
ax = fig.add_subplot(111)
lines = ax.plot(data)
ax.legend(['channel {}'.format(c) for c in range(ch_num)],
          loc='lower left', ncol=4,
          bbox_to_anchor=(0., 1.02, 1., .102))
plt.show()
