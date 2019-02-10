import argparse
import queue
import sys
import numpy as np
from scipy.signal.waveforms import sweep_poly
from scipy import signal


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text
def generate_chirp():
    p = np.poly1d([1.4, 16])
    t = np.linspace(0, 5, 5*48)
    w = sweep_poly(t, p)
    w = np.hanning(len(w))*w
    up_chirp = np.copy(w)

    p = np.poly1d([-1.4, 30])
    t0 = np.linspace(5, 10, 5*48)
    t = np.append(t, t0)
    w0 = sweep_poly(t0, p)
    w0 = np.hanning(len(w0))*w0
    w = np.append(w, w0)
    down_chirp = np.copy(w0)

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

    return w, up_chirp, down_chirp
y, up_chirp, down_chirp = generate_chirp()
left_y = np.append(y, np.zeros(10*48))
right_y = np.append(np.zeros(10*48), y)

y = y.reshape(len(y), 1)
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
    '-i', '--interval', type=float, default=30,
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

def audio_callback(indata, outdata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    # if status:
    #     print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::args.downsample, mapping])
    # global i
    # l = len(outdata[:, 0])
    # print(i, i+l)
    # if i+l >= len(left_y):
    #     outdata[:, 0] = np.append(left_y[i:], left_y[:i+l-len(left_y)])
    #     outdata[:, 1] = np.append(right_y[i:], right_y[:i+l-len(right_y)])
    #     i = i+l-len(left_y)
    # else:   
    #     outdata[:, 0] = left_y[i:i+l]
    #     outdata[:, 1] = right_y[i:i+l]
    #     i += l
    outdata[:] = y

def update_plot(frame):
    """This is called by matplotlib for each plot update.

    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.

    """
    global plotdata, sos, up_chirp, down_chirp
    while True:
        try:
            data = q.get_nowait()
            # ind = signal.sosfilt(sos, ind)
            for i in range(data.shape[1]):
                data[i] = signal.sosfilt(sos, data[i])
                if i%2 == 0:
                    data[i] = signal.correlate(data[i], down_chirp, mode='same')
                else:
                    data[i] = signal.correlate(data[i], up_chirp, mode='same')
        except queue.Empty:
            break
        shift = len(data)
        # print(shift)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    if np.max(plotdata) > 0.25:
        np.savetxt('plotdata.txt', plotdata)
    for column, line in enumerate(lines):
        line.set_ydata(np.absolute(plotdata[:, column]))
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

    length = int(args.window * args.samplerate / (1000 * args.downsample))
    # print(length)
    plotdata = np.zeros((length, len(args.channels)))

    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)
    if len(args.channels) > 1:
        ax.legend(['channel {}'.format(c) for c in args.channels],
                  loc='lower left', ncol=len(args.channels))
    ax.axis((0, len(plotdata), -1, 1))
    # ax.set_yticks([0])
    # ax.yaxis.grid(True)
    # ax.tick_params(bottom='off', top='off', labelbottom='off',
    #                right='off', left='off', labelleft='off')
    fig.tight_layout(pad=0)

    stream = sd.Stream(
        device=(0, 1), channels=max(args.channels), blocksize=960,
        samplerate=args.samplerate, callback=audio_callback)
    ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=True)
    with stream:
        plt.show()
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))