#!/bin/sh
echo 'installing dependencies ...'

sudo apt-get install -y build-essential python3 python3-pip python3-pyaudio \
python3-numpy python3-pyqt4 python3-setuptools

pip3 install --user pyqtgraph

echo 'done'
