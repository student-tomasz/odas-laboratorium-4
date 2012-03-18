#!/usr/bin/env python

import sys, fileinput

class MyARC4:
    def __init__(self, key):
        self.key = key
        self.reg = range(256)
        j = 0
        for i in range(256):
            j = (j + self.reg[i] + ord(self.key[i%len(self.key)])) % len(self.reg)
            self.reg[j], self.reg[i] = self.reg[i], self.reg[j]

    def encrypt(self, plaintext):
        encrypted = ''
        i, j = 0, 0
        for char in plaintext:
            i = (i + 1) % len(self.reg)
            j = (j + self.reg[i]) % len(self.reg)
            self.reg[j], self.reg[i] = self.reg[i], self.reg[j]
            key_char = self.reg[(self.reg[i] + self.reg[j]) % len(self.reg)]
            encrypted += chr(ord(char) ^ key_char)
        return encrypted

def new(key):
    return MyARC4(key)
