from PyQt4 import QtGui, QtCore

import sys
import ui_main
import numpy as np
import pyqtgraph
import SWHear


count = 0

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        # before loading widget
        pyqtgraph.setConfigOption('background', 'w')
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.grFFT.plotItem.showGrid(True, True, 0.7)
        self.grPCM.plotItem.showGrid(True, True, 0.7)
        self.maxFFT = 0
        self.maxPCM = 0
        self.oldfft = []
        self.oldfftx = []
        self.ear = SWHear.SWHear(rate=44100, updatesPerSecond=10)
        self.ear.stream_start()

    def update(self):
        origin = '\x1b[0m'
        red = '\x1b[31m'
        frqlist = []
        frvlist = []
        timeseq = []
        if self.ear.data is not None and self.ear.fft is not None:
            pcmMax = np.max(np.abs(self.ear.data))

            if pcmMax > self.maxPCM:
                self.maxPCM = pcmMax
                self.grPCM.plotItem.setRange(yRange=[-pcmMax, pcmMax])

            if np.max(self.ear.fft) > self.maxFFT:
                self.maxFFT = np.max(np.abs(self.ear.fft))

                # self.grFFT.plotItem.setRange(yRange=[0, self.maxFFT])
                self.grFFT.plotItem.setRange(yRange=[0, 100000000])

            self.pbLevel.setValue(1000*pcmMax/self.maxPCM)
            pen = pyqtgraph.mkPen(color='b')
            self.grPCM.plot(self.ear.datax,
                            self.ear.data,
                            pen=pen,
                            clear=True)

            pen = QtGui.QPen(QtGui.QColor(255, 108, 0))
            # print(self.ear.data)
            if len(self.oldfft) == 0:
                self.oldfft = self.ear.fft
            else:
                if pcmMax < 15000:
                    # No extrem sound
                    for ft, fx, oft in zip(self.ear.fft, self.ear.fftx, self.oldfft):
                        if fx >= 19900 and fx <= 20100:
                            #times = abs(ft - oft)
                            #if times > 200000:
                            times = float(ft/oft)
                            if times > 1.3 and ft > 5000:
                                frqlist.append(fx)
                                frvlist.append(ft-oft)
                                timeseq.append(times)


                    self.oldfft = self.ear.fft
                    if len(frqlist) > 13:
                        global count
                        count += 1
                        with open('left.txt', 'w') as f:
                            f.write("\n")
                            f.write("{}{:^7}{}  {:^13}  {:^13} {}{:^7}{}".format(red, 'Times', origin, 'Frequency', 'Value', red, 'TIMES', origin))
                            for frq, frv, tq in zip(frqlist, frvlist, timeseq):
                                f.write("%s%7d%s %12.2f  %12.2f  %s%7.2f%s" % (red, count, origin, frq, frv, red, tq, origin))
                        print("\n")
                        print("=======================================")
                        print("{}I heard that you've waved your hands!{}".format(red, origin))
                        print("=======================================")
                        print('\n')
                    frqlist = []
                    frvlist = []
                    timeseq = []

            self.grFFT.plot(self.ear.fftx,
                            self.ear.fft,
                            pen=pen,
                            clear=True)

        # QUICKLY repeat
        QtCore.QTimer.singleShot(5, self.update)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    # start with something
    form.update()
    app.exec_()
    print("DONE")
