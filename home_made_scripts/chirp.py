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
        outdata[:, 1] = y

with sd.Stream(device=(0, 1),
               callback=callback,
               blocksize=960,
               samplerate=48000):
	print('#' * 80)
	print('press Return to quit')
	print('#' * 80)
	input()
