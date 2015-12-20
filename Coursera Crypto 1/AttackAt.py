#!/usr/bin/python2



'''
6c73d5240a948c86981bc294814d 

attack at dawn

attack at dusk
'''


def strxor( a, b):     # xor two strings of different lengths
        if len(a) > len(b):
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
        else:
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

ct1="6c73d5240a948c86981bc294814d"
pt1="attack at dawn"
pt2="attack at dusk"

k=strxor(pt1,ct1.decode("hex"))
ct2=strxor(pt2,k).encode("hex")

print format("k: %s " % k.encode("hex"))
print format("ct1: %s" % ct1)
print format("ct2: %s" % ct2)
