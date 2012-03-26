#!/usr/bin/env python

import math, string, sys

def count_bytes(data):
    bytes = {}
    for byte in data:
        if not byte in bytes:
            bytes[byte] = 0
        bytes[byte] += 1
    for byte in bytes:
        bytes[byte] = float(bytes[byte]) / float(len(data))
        # print "%s => %g" % (char, chars[char])
    return bytes

def count_entropy(filepath):
    bytes = count_bytes(open(filepath, 'rb').read())
    entropy = 0
    for byte in bytes:
        entropy -= bytes[byte] * math.log(bytes[byte], 2)
    return entropy

print count_entropy(sys.argv[1])
