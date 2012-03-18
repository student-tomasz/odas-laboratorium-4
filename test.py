#!/usr/bin/env python

import sys
from Crypto.Cipher import ARC4
from lib import MyARC4

key = sys.argv[1]
plaintext_file = open(sys.argv[2], 'r')
plaintext = plaintext_file.read()
plaintext_file.close()

encrypted = {}
for cipher in [ARC4, MyARC4]:
    encrypted[cipher] = cipher.new(key).encrypt(plaintext)

if encrypted[MyARC4] == encrypted[ARC4]:
    print 'passed'
else:
    print 'failed'

if plaintext == ARC4.new(key).decrypt(encrypted[MyARC4]):
    print 'passed'
else:
    print 'failed'
