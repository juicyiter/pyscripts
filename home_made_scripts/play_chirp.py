import argparse
import sounddevice as sd
import pickle
import numpy as np
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    'odd', type=str,
    help='odd channel input data (numpy array like)')
parser.add_argument(
    'even', type=str,
    help='odd channel input data (numpy array like)')
args = parser.parse_args()

odd_y = pickle.load(open(args.odd, 'rb'))
even_y = pickle.load(open(args.even, 'rb'))

out = np.append(odd_y, even_y)
out = out.reshape(len(odd_y), -1)

def callback(outdata, frames, time, status):
    outdata[:, 0] = odd_y
    outdata[:, 1] = even_y

with sd.OutputStream(samplerate=48000, blocksize=1200,
                        channels=2, dtype='float32', device=0,
                        callback=callback):
    input()
