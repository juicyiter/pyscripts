#!/opt/local/bin/python
# _*_ coding: utf-8 _*_

''' Show files in current directory and sub-directories,
whose name contains specifiec name.

Be careful of "NON OPTION STATE" like no option and name at all!

Because it will list all the files in current and sub directories!'''

__author__ = 'Ethan Mengoreo'

import os
import argparse


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-l', '--fname', type=int_or_str,
                    help='list files whose name contains fname')
args = parser.parse_args()


cur = os.environ.get('PWD')
flag = 0
red = '\x1b[31m'
origin = '\x1b[0m'

if not args.fname:
    args.fname = ''


def do_dir(di, fname=args.fname):
    '''
    >>> do_dir(cur, 'test')
    ./testaudio.py
    ./doc_test.py
    ./test.log
    ./test.py
    ./__pycache__/doc_test.cpython-37.pyc
    '''
    global cur, flag
    os.chdir(di)

    for f in [x for x in os.listdir('.') if os.path.isfile(x)]:
        if f.__contains__(fname):
            # Highlight fname
            start = f.find(fname)
            end = start + len(fname)
            f = f[0:start] + red + fname + origin + f[end:]
            # Conver current directory to .
            current = di.replace(cur, '.')
            f = os.path.join(current, f)
            print(f)
            flag = 1

    for dire in [d for d in os.listdir('.') if os.path.isdir(d)]:
        dire = os.path.join(di, dire)
        do_dir(dire, fname)



if __name__ == '__main__':
    do_dir(cur)
    if not flag:
        print('Not Found!')
