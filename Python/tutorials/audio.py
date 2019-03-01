import pyaudio
import numpy as np
import pylab
import time

RATE = 44100
CHUNK = 2048  # RATE / number of updates per second

def soundplot(stream):
    t1=time.time()
    data = stream.read(CHUNK)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    pylab.axis([0,len(data),-2**16/2,2**16/2])
    pylab.savefig("03.png",dpi=50)
    pylab.close('all')
    print("took %.02f ms"%((time.time()-t1)*1000))

if __name__=="__main__":
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)
    for i in range(0, CHUNK): #do this for 10 seconds
        soundplot(stream)

    stream.stop_stream()
    stream.close()
    p.terminate()
