#!/usr/bin/python

import sys

'''
MSGS = ( 
"hola amigo",
"hola enemigo",
"chau amigo",
)
'''

MSGS = ( 
"   ",
"uno",
"UNO",
"123"
)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    for char in msg:
        sys.stdout.write(char + " ")
#    print 
    print c.encode('hex')
    return c
def show(msg,cipher):
    msgBin = ' '.join(format(ord(x), 'b') for x in msg)
    cipherBin = ' '.join(format(ord(x), 'b') for x in cipher)

    print format("msg: %s msgAscii: %s msgBin: %s cipherHex: %s cipherBin: %s" % ( msg , msg.encode('hex'), msgBin, cipher.encode('hex'), cipherBin))


def main():
    key = random(1024)
    ciphertexts =[]
    for msg in MSGS:
        ciphertexts.append(strxor(key,msg))

    print "------------------------------------"
    print
    print "key   " + key.encode('hex')[0:6]
    print show( MSGS[0] ,ciphertexts[0])
    print show( MSGS[1] ,ciphertexts[1])
    print show( MSGS[2] ,ciphertexts[2])
    print show( MSGS[3] ,ciphertexts[3])
    print
    print "------------------------------------"

    print
    print "1 y 3 " + strxor(ciphertexts[1],ciphertexts[3]).encode('hex')
#    print "0 y 2 " + strxor(ciphertexts[1])
#    print "0 y 3 " + strxor(ciphertexts[2])
main()
