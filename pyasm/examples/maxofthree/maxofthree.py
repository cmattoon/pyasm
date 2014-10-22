#!/usr/bin/python
import sys, ctypes

def maxofthree():             # See function 'maxofthree' in maxofthree.asm
    global rdi, rsi, rdx
    rax = rdi                 # sys.argv[1]

    if rax < rsi:             # sys.argv[2]
        rax = rsi

    if rax < rdx:             # sys.argv[3]
        rax = rdx

    return rax

def main(): # See function 'main' in maxofthree.c
    global rdi, rsi, rdx

    rdi, rsi, rdx = [1, -4, -7] 
    print("%d" % maxofthree())

    rdi, rsi, rdx = [2, -6, 1]
    print("%d" % maxofthree())

    rdi, rsi, rdx = [3, 2, 1]
    print("%d" % maxofthree())

    rdi, rsi, rdx = [-2, 4, 3]
    print("%d" % maxofthree())

    rdi, rsi, rdx = [2, -6, 5]
    print("%d" % maxofthree())

    rdi, rsi, rdx = [2, 4, 6]
    print("%d" % maxofthree())

    exit(0)

if __name__ == "__main__":
    """ Initialize registers (just because)
    """
    rax = ctypes.c_int(64)
    rdx = ctypes.c_int(64)
    rdi = ctypes.c_int(64)
    rsi = ctypes.c_int(64)

    main()


