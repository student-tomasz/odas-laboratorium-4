#!/usr/bin/env python

from Crypto.Cipher import ARC4
import sys, fileinput


key = sys.argv[1]
encrypted_file = open(sys.argv[2], 'r+')

cipher = ARC4.new(key)
print cipher.decrypt(encrypted_file.read())

encrypted_file.close()
