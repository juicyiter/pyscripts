import argparse
import queue
import sys
import numpy as np
from scipy.signal.waveforms import sweep_poly
from scipy import signal
import pickle


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def generate_chirp():
    p = np.poly1d([7, 16])
    t = np.linspace(0, 1, 1*48)
    w = sweep_poly(t, p)
    w = np.hanning(len(w))*w
    up_chirp = np.copy(w)
    left_y = np.copy(w)
    right_y = np.zeros(1*48)

    p = np.poly1d([-7, 30])
    t0 = np.linspace(1, 2, 1*48)
    t = np.append(t, t0)
    w0 = sweep_poly(t0, p)
    w0 = np.hanning(len(w0))*w0
    w = np.append(w, w0)
    down_chirp = np.copy(w0)
    left_y = np.append(left_y, np.zeros(48))
    right_y = np.append(right_y, w0)

    return left_y, right_y, up_chirp, down_chirp


left_y, right_y, up_chirp, down_chirp = generate_chirp()
left_y = np.append(left_y, np.zeros(18*48))
pickle.dump(left_y, open('left_y.pickle', 'wb'))
# right_y = np.append(np.zeros(1*48), y)
right_y = np.append(right_y, np.zeros(18*48))
pickle.dump(right_y, open('right_y.pickle', 'wb'))

# y = y.reshape(len(y), 1)
sos = signal.butter(10, [16000, 23000], 'bandpass', fs=48000, output='sos')


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-w', '--window', type=float, default=20, metavar='DURATION',
    help='visible time slot (default: %(default)s ms)')
parser.add_argument(
    '-i', '--interval', type=float, default=20,
    help='minimum time between plot updates (default: %(default)s ms)')
parser.add_argument(
    '-b', '--blocksize', type=int, help='block size (in samples)')
parser.add_argument(
    '-r', '--samplerate', type=float, help='sampling rate of audio device')
parser.add_argument(
    '-n', '--downsample', type=int, default=1, metavar='N',
    help='display every Nth sample (default: %(default)s)')
parser.add_argument(
    'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    help='input channels to plot (default: the first)')
args = parser.parse_args()
if any(c < 1 for c in args.channels):
    parser.error('argument CHANNEL: must be >= 1')
mapping = [c - 1 for c in args.channels]  # Channel numbers start with 1
q = queue.Queue()

args.samplerate = 48000
i = 0

output_file = open('output.txt', 'w')
def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::args.downsample, mapping])


def callback(outdata, frames, time, status):
    outdata[:, 0] = left_y[::args.downsample]
    outdata[:, 1] = right_y[::args.downsample]


def update_plot(frame):
    """This is called by matplotlib for each plot update.

    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.

    """
    global plotdata, sos, up_chirp, down_chirp, flag
    while True:
        try:
            data = q.get_nowait()
            # ind = signal.sosfilt(sos, ind)
            # data = np.append(data, data, axis=1)
            flag = 0
            
            for i in range(data.shape[1]):
                data[:, i] = signal.sosfilt(sos, data[:, i])
                flag = i%2
                if flag == 0:

                    data[:, i] = signal.correlate(data[:, i],
                                                  up_chirp, mode='same')
                else:
                    data[:, i] = signal.correlate(data[:, i],
                                                  down_chirp, mode='same')
                data[:, i] = np.absolute(signal.hilbert(data[:, i]))
                pdata = data[:, i]
                peaks, _ = signal.find_peaks(pdata, distance=50)
                pvalues = pdata[peaks]
                max_two_index = pvalues.argsort()[-2:][::-1]
                fir, sec = max_two_index[0], max_two_index[1]
##                if 2*pvalues[sec] > pvalues[fir]:
##                    distance = np.absolute(peaks[fir] - peaks[sec])
##                    if distance > 480:
##                        distance = 960 - distance
##                    if distance > 90 and distance < 100:
##                        print('==============================')
##                        print("Index difference of {}:".format(flag), distance)
##                        print('==============================')
##                        print()
##                        print()
                distance = np.absolute(peaks[fir] - peaks[sec])
                print(distance, file=output_file)
                
        except queue.Empty:
            break
        shift = len(data)
##        np.savetxt('plotdata.txt', data)
        plotdata = np.roll(plotdata, -shift, axis=0)

        plotdata[-shift:, :] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
    return lines


try:
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt
    import numpy as np
    import sounddevice as sd

    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        args.samplerate = device_info['default_samplerate']
    # length = len(left_y)
    length = int(args.window * args.samplerate / (1000 * args.downsample))
    print(length)
    plotdata = np.zeros((length, len(args.channels)))
    # plotdata = np.append(plotdata, plotdata, axis=1)

    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)
    # if len(args.channels) > 1:
    if 1:
        ax.legend(['channel {}'.format(c) for c in [1, 2]],
                  loc='lower left', ncol=len(args.channels))
    ax.axis((0, len(plotdata), 0, 1.5))
    # ax.set_yticks([0])
    # ax.yaxis.grid(True)
    # ax.tick_params(bottom='off', top='off', labelbottom='off',
    #                right='off', left='off', labelleft='off')
    fig.tight_layout(pad=0)

    stream = sd.InputStream(
        device=args.device, channels=max(args.channels), blocksize=length,
        samplerate=args.samplerate, callback=audio_callback)
    ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=True)

    with stream:
        with sd.OutputStream(samplerate=48000, blocksize=length,
                             channels=2, dtype='float32', device=0,
                             callback=callback):
            plt.show()
    output_file.close()
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
