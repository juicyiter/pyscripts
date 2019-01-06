from PyQt5 import QtGui, QtCore

import sys
import ui_main
import numpy as np
import pyqtgraph
import SWHear


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
        self.ear = SWHear.SWHear(rate=44100, updatesPerSecond=5)
        self.ear.stream_start()

    def update(self):
        if self.ear.data is not None and self.ear.fft is not None:
            pcmMax = np.max(np.abs(self.ear.data))

            if pcmMax > self.maxPCM:
                self.maxPCM = pcmMax
                self.grPCM.plotItem.setRange(yRange=[-pcmMax, pcmMax])

            if np.max(self.ear.fft) > self.maxFFT:
                self.maxFFT = np.max(np.abs(self.ear.fft))
                # self.grFFT.plotItem.setRange(yRange=[0, self.maxFFT])
                self.grFFT.plotItem.setRange(yRange=[0, 0.05])

            self.pbLevel.setValue(1000*pcmMax/self.maxPCM)
            pen = pyqtgraph.mkPen(color='b')
            self.grPCM.plot(self.ear.datax,
                            self.ear.data,
                            pen=pen,
                            clear=True)

            pen = pyqtgraph.mkPen(color='r')
            print()
            print(self.ear.fftx, len(self.ear.fftx))
            print(self.ear.data, len(self.ear.data))
            print(self.ear.fft/self.maxFFT, len(self.ear.fft))
            print()
            self.grFFT.plot(self.ear.fftx,
                            self.ear.fft/self.maxFFT,
                            pen=pen,
                            clear=True)

        # QUICKLY repeat
        QtCore.QTimer.singleShot(1, self.update)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    # start with something
    form.update()
    app.exec_()
    print("DONE")
