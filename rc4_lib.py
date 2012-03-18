#!/usr/bin/env python

from Crypto.Cipher import ARC4
import sys, fileinput


key = sys.argv[1]
plaintext_file = open(sys.argv[2], 'r+')
encrypted_file = open(sys.argv[3], 'w+')
encrypted = ''

cipher = ARC4.new(key)
encrypted_file.write(cipher.encrypt(plaintext_file.read()))

plaintext_file.close()
encrypted_file.close()
