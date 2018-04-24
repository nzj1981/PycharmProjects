#!/usr/bin/env python3
#encoding:utf-8

from multiprocessing import Process
import os, time

#child process execute code
def run_proc(name):
    time.sleep(10)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process wild start.')
    p.start()
    p.join()
    p = Process(target=run_proc, args=('test1',))
    print('Child process wild start.')
    p.start()
    p.join()
    p = Process(target=run_proc, args=('test2',))
    print('Child process wild start.')
    p.start()
    p.join()
    print('Child process end')
