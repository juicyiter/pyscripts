import sounddevice as sd
import numpy as np
import pickle
with open('chirp.pickle', 'rb') as f:
	y = pickle.load(f)
input_device = 0
i = 0
device_list = list(sd.query_devices())
for device in device_list:
	if device['max_input_channels'] == 4:
		input_device = device_list.index(device)
		break

def callback(indata, outdata, frames, time, status):
        global i
        outdata[:, 1] = y[i:i+500]
        i += 500
        if i >= len(y):
                i = 0

with sd.Stream(device=(input_device, 0),
               callback=callback,
               blocksize=500,
               samplerate=44100):
	print('#' * 80)
	print('press Return to quit')
	print('#' * 80)
	input()
