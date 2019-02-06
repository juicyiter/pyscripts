#!/usr/bin/env python3
"""Plot the live microphone signal(s) with matplotlib.

Matplotlib and NumPy have to be installed.

"""
import argparse
import queue
import sys
import pickle
chirp = pickle.load(open('chirp.pickle', 'rb'))

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-w', '--window', type=float, default=200, metavar='DURATION',
    help='visible time slot (default: %(default)s ms)')
parser.add_argument(
    '-i', '--interval', type=float, default=50,
    help='minimum time between plot updates (default: %(default)s ms)')
parser.add_argument(
    '-b', '--blocksize', type=int, help='block size (in samples)')
parser.add_argument(
    '-r', '--samplerate', type=float, help='sampling rate of audio device')
parser.add_argument(
    '-n', '--downsample', type=int, default=10, metavar='N',
    help='display every Nth sample (default: %(default)s)')
parser.add_argument(
    'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    help='input channels to plot (default: the first)')
args = parser.parse_args()
if any(c < 1 for c in args.channels):
    parser.error('argument CHANNEL: must be >= 1')
mapping = [c - 1 for c in args.channels]  # Channel numbers start with 1
q = queue.Queue()


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::args.downsample, mapping])


def update_plot(frame):
    """This is called by matplotlib for each plot update.

    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.

    """
    global plotdata, maxfft
    tempdata = np.ndarray(shape=(1, plotdata.shape[1]))
    # print(tempdata)
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
        tempdata = np.append(tempdata, data, axis=0)

    # delete first row of initial values
    tempdata = np.roll(tempdata, -1, axis=0)

    # IMPORTANT!!!!
    # tempdata = tempdata.reshape(len(tempdata),)
    # print(tempdata)
    # np.savetxt('temp.txt', tempdata)
    for i in range(len(args.channels)):
        coldata = tempdata[:, i]
        coldata[coldata == np.inf] = 0.0
        coldata[coldata > 1] = 0.0
        coldata = coldata.reshape(len(coldata), )
        tempfft = np.fft.fft(coldata)
        tempfft = np.abs(tempfft)
        tempfreq = np.fft.fftfreq(len(tempfft), 1.0/44100)
        tempfft = tempfft[:int(len(tempfft)/2)]
        # if maxfft[i] > 0:
        #     tempfft = tempfft / maxfft[i]
        # try:
        #     if np.max(tempfft) > maxfft[i]:
        #         maxfft[i] = np.max(tempfft)

        # except ValueError:
        #     pass
        tempfreq = tempfreq[:int(len(tempfreq)/2)]
        if i == 0:
            fft = None
            freq = None
            fft = tempfft
            fft = fft.reshape(len(fft), 1)
            freq = tempfreq
            freq = freq.reshape(len(freq), 1)
        else:
            gap = len(tempfft) - fft.shape[0]
            if gap > 0:
                fft = np.append(np.zeros(gap-1, fft.shape[1]), fft, axis=0)
                freq = np.append(np.zeros(gap-1, fft.shape[1]), freq, axis=0)
            elif gap < 0:
                tempfft = np.append(np.zeros(-gap-1,), tempfft, axis=0)
                tempfreq = np.append(np.zeros(-gap-1,), tempfreq, axis=0)

            tempfft = tempfft.reshape(len(tempfft), 1)
            tempfreq = tempfreq.reshape(len(tempfreq), 1)
            # print(fft.shape, tempfft.shape)
            fft = np.append(fft, tempfft, axis=1)
            freq = np.append(freq, tempfreq, axis=1)

    # if len(fft) > 0 and np.max(fft) > 1:
    #     print()
    #     print(fft)
    #     print()
    #     print(tempdata)
    #     # sys.exit(1)
    # print(len(args.channels))
    # for i in range(len(args.channels)):
    #     coldata = tempdata[:, i]
    #     coldata = coldata.reshape(len(coldata), )
    #     coldata[coldata == np.inf] = 0.0
    #     # print(coldata.shape)
    #     fft = np.fft.fft(coldata)
    #     fft = np.abs(fft)
    #     freq = np.fft.fftfreq(len(fft), 1.0/44100)
    #     fft = fft[:int(len(fft)/2)]
    #     freq = freq[:int(len(freq)/2)]
    #     print()
    #     print(fft)
    #     print()
    #     flines[i].set_data(freq, fft)

    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
    # for line in enumerate(flines):
    np.savetxt('fft.txt', fft)
    np.savetxt('freq.txt', freq)
    # flines.set_data(freq, fft)
    for i in range(len(flines)):
        flines[i].set_data(freq[:, i], fft[:, i])
    return lines, flines,


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
    plotdata = np.zeros((length, len(args.channels)))

    maxfft = np.zeros((len(args.channels), ))
    fft = np.zeros((length, len(args.channels)))
    freq = np.zeros((length, len(args.channels)))
    # fig, (ax, fx) = plt.subplots(1, 2, sharey=True)
    fig = plt.figure(1)

    # lines
    ax = fig.add_subplot(121)
    fx = fig.add_subplot(122)

    lines = ax.plot(plotdata)
    flines = fx.plot(freq, fft)
    # flines = []
    # for i in range(len(args.channels)):
    #     flines.append(fx.plot(freq, fft)[0])

    # Colors
    if len(args.channels) > 1:
        ax.legend(['channel {}'.format(c) for c in args.channels],
                  loc='lower left', ncol=len(args.channels),
                  bbox_to_anchor=(0., 1.02, 1., .102))
        fx.legend(['channel {}'.format(c) for c in args.channels],
                  loc='lower left', ncol=len(args.channels),
                  bbox_to_anchor=(0., 1.02, 1., .102))

    ax.axis((0, len(plotdata), -1, 1))
    fx.axis((0, 44100, -0.5, 1.5))
    # ax.set_yticks([0])
    ax.yaxis.grid(True)
    fx.yaxis.grid(True)
    # ax.tick_params(bottom='off', top='off', labelbottom='off',
    #                right='off', left='off', labelleft='off')
    fig.tight_layout(pad=0)

    stream = sd.InputStream(
        device=args.device, channels=max(args.channels),
        samplerate=args.samplerate, callback=audio_callback)
    ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=False)
    with stream:
        plt.show()
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
