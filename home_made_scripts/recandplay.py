import sounddevice as sd
import time
import matplotlib.pyplot as plt
import subprocess
import numpy as np

cumulated_status = sd.CallbackFlags()
f1 = open('none0.txt', 'w')
f2 = open('none1.txt', 'w')
f3 = open('none2.txt', 'w')
count = 0

def show(data):
    global count
    #plt.ion()
    print('\n\n')
    print('About to recording next sec...')
    print('Get ready')
    time.sleep(1)
    
    # fig = plt.figure(3)
    # row1 = fig.add_subplot(411, autoscalex_on=True)
    # row2 = fig.add_subplot(412, autoscalex_on=True)
    # row3 = fig.add_subplot(413, autoscalex_on=True)
    # row4 = fig.add_subplot(414, autoscalex_on=True)
    # row1.clear()
    # row2.clear()
    # row3.clear()
    # row4.clear()
    if count == 1:
        np.savetxt(f1, data, fmt=['%1.7f', '%1.7f', '%1.7f', '%1.7f'],
                   delimiter=' ', newline='\n')
        print('Done')
    elif count == 2:
        np.savetxt(f2, data, fmt=['%1.7f', '%1.7f', '%1.7f', '%1.7f'],
                   delimiter=' ', newline='\n')
        print('Done')
    elif count == 3:
        np.savetxt(f3, data, fmt=['%1.7f', '%1.7f', '%1.7f', '%1.7f'],
                   delimiter=' ', newline='\n')
        print('Done')
    elif count > 3:
        return 0
    # row1.plot(data[:,0])
    # row2.plot(data[:,1])
    # row3.plot(data[:,2])
    # row4.plot(data[:,3])
    
    # fig.canvas.draw()

    count += 1
    return 1

def plotdata(indata, frames, time, status):
    # print while InputStream calling back
    global cumulated_status
    cumulated_status |= status
    flag = show(indata)
    if not flag:
        exit(0)

with sd.InputStream(blocksize=44100, device=2, channels=4, callback=plotdata):
    play = ['python', 'play.py']
    sd.default.device = 0
    subprocess.run(play)
    while(1):

        exit(1)
