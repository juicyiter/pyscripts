import sounddevice as sd
import numpy as np
import pickle
from scipy.signal.waveforms import sweep_poly


def generate_chirp():
	p = np.poly1d([1.4, 16])
	t = np.linspace(0, 5, 5*48)
	w = sweep_poly(t, p)
	w = np.hanning(len(w))*w

	p = np.poly1d([-1.4, 30])
	t0 = np.linspace(5, 10, 5*48)
	t = np.append(t, t0)
	w0 = sweep_poly(t0, p)
	w0 = np.hanning(len(w0))*w0
	w = np.append(w, w0)

	p = np.poly1d([1.4, 2])
	t0 = np.linspace(10, 15, 5*48)
	t = np.append(t, t0)
	w0 = sweep_poly(t0, p)
	w0 = np.hanning(len(w0))*w0
	w = np.append(w, w0)

	p = np.poly1d([-1.4, 44])
	t0 = np.linspace(15, 20, 5*48)
	t = np.append(t, t0)
	w0 = sweep_poly(t0, p)
	w0 = np.hanning(len(w0))*w0
	w = np.append(w, w0)
	w = w*0.8

	return w

y = generate_chirp()
y = np.array(y)
# with open('chirp.pickle', 'rb') as f:
# 	y = pickle.load(f)
input_device = 0
i = 0
device_list = list(sd.query_devices())
for device in device_list:
	if device['max_input_channels'] == 4:
		input_device = device_list.index(device)
		break



def callback(indata, outdata, frames, time, status):
        global i
        outdata = y

with sd.RawStream(device=(0, 1),
               callback=callback,
               blocksize=960,
               samplerate=48000):
	print('#' * 80)
	print('press Return to quit')
	print('#' * 80)
	input()
