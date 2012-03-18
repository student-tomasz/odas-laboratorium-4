#!/usr/bin/env python

import string, subprocess, sys, time
from Crypto.Cipher import ARC4
from lib import MyARC4

key = string.ascii_lowercase
sizes = [6, 60, 600, 2000, 4000, 6000]
ciphers = [ARC4, MyARC4]
times = {}
sample_filepath = 'samples/plain_{0}k.txt'
plt_filepath = 'times.plt'
dat_filepath = 'times.dat'

def measure():
    for size in sizes:
        times[size] = {}
        for cipher in ciphers:
            plaintext_file = open(sample_filepath.format(size), 'r')
            start = time.clock()
            cipher.new(key).encrypt(plaintext_file.read())
            times[size][cipher] = time.clock() - start
            plaintext_file.close()

def write():
    plt_file = open(plt_filepath, 'w')
    plt_file.write('set key left top\n')
    plt_file.write('set grid\n')
    plt_file.write('set xrange [0:6500]\n')
    plt_file.write('plot\\\n')
    for cipher in ciphers:
        plt_file.write('  "{0}" using 1:{2} title "{1}" with points'.format(dat_filepath, cipher.__name__, ciphers.index(cipher)+2))
        if cipher != ciphers[-1]:
            plt_file.write(',\\\n')
        else:
            plt_file.write('\n')
    plt_file.write('pause -1\n')
    plt_file.close()

    dat_file = open(dat_filepath, 'w')
    for size in sizes:
        dat_file.write('{0:4d} {1:8f} {2:8f}\n'.format(size, times[size][ARC4], times[size][MyARC4]))
    dat_file.close()

def draw():
    subprocess.call(['gnuplot', plt_filepath])

measure()
write()
draw()
