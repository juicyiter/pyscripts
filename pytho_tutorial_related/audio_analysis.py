# coding: utf-8

import wave
import pyaudio as pa
import numpy as np
import pylab

wf = wave.open('/Users/mengoreo/Desktop/Tone20K.wav', 'rb')

p = pa.PyAudio()
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
nframes = wf.getnframes()
framerate = wf.getframerate()

# 读取完整的帧数据到 str_data 中，
# 这是一个 string 类型的数据

str_data = wf.readframes(nframes)
wf.close()

# 将波形数据转换成数组

wave_data = np.frombuffer(str_data, dtype = np.short)

# 将 wave_data 数组转换成 2 列，行数自动匹配。
# 在修改 shape 属性时，需要使得数组的总长度不变

wave_data.shape = -1, 2

wave_data = wave_data.T

N = 44100
start = 0
df = framerate / (N - 1)
freq = [df * n for n in range(0, N)]
wave_data2 = wave_data[0][start : start + N]
c = np.fft.fft(wave_data2) * 2 / N
d = int(len(c) / 2)
while freq[d] > 4000:
    d -= 10

pylab.plot(freq[:d - 1], abs(c[:d - 1]), 'r')
pylab.show()
