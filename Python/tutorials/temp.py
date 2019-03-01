from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s) ...' % (name, os.getpid()))


if __name__ == '__main__':
    p = Process(target=run_proc, args=('test',))
    print('Parent process is %s.' % os.getpid())
    print('Starting child process...')
    p.start()

    print('Started')
    print('Joining')
    p.join()
    print('Ended')
