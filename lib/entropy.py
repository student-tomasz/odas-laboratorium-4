#!/usr/bin/env python

import math, string, sys

def count_chars(filepath):
    chars = {}
    count = 0
    for char in string.ascii_lowercase + ' ':
        chars[char] = 0
    for char in open(filepath, 'r').read():
        char = char.lower()
        if char in chars:
            count += 1
            chars[char] += 1
    for char in chars:
        chars[char] = float(chars[char]) / float(count)
        # print "%s => %g" % (char, chars[char])
    return chars

def count_entropy(filepath):
    entropy = 0
    chars = count_chars(filepath)
    for char in chars:
        if chars[char] <= 0:
            continue
        entropy -= chars[char] * math.log(chars[char], 2)
    return entropy

print count_entropy(sys.argv[1])
