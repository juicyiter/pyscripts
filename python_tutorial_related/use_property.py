#!/opt/local/bin/python
# _*_ coding: utf-8 _*_

' '

__author__ = 'Ethan Mengoreo'

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height

print(__name__)

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution = ', s.resolution)
