#!/usr/bin/env python

import sys, fileinput

def generate_register(key):
    register = range(256)
    j = 0
    for i in range(256):
        j = (j + register[i] + ord(key[i%len(key)])) % len(register)
        register[j], register[i] = register[i], register[j]
    return register

def rc4():
    key = sys.argv[1]
    plaintext_file = open(sys.argv[2], 'r+')
    encrypted_file = open(sys.argv[3], 'w+')
    encrypted = []

    register = generate_register(key)
    i = 0
    j = 0
    for char in plaintext_file.read():
        i = (i + 1) % len(register)
        j = (j + register[i]) % len(register)
        register[j], register[i] = register[i], register[j]
        key_char = register[(register[i] + register[j]) % len(register)]
        encrypted.append(chr(ord(char) ^ key_char))
    encrypted_file.write(''.join(encrypted))

    plaintext_file.close()
    encrypted_file.close()

rc4()
