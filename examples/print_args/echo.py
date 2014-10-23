#!/usr/bin/python
import sys, ctypes
"""
rdi contains argc
rsi contains argv (in reverse) - Note rdi decrements


"""
def echo_args():             # See function 'echo_args' in echo.asm
    global rdi, rsi, rdx, stack
    stack.append(rdi) # "push"
    stack.append(rsi) # "push"
    ## Stack alignment?? rsp = index or something?

    rdi = rsi[rdi-1] # Take next arg.. they keep getting popped (below)
    puts()

    ## add rsp, 8 --- Restore stack. Need to implement stack class or something
    ## to really illustrate it.
    rsi = stack.pop()
    rdi = stack.pop()
    
    rsi.pop()
    rdi -= 1

    if rdi != 0:
        echo_args()

    return rax # Exit code 0?

def puts():
    print rdi

def main(): # See function 'main' in maxofthree.c
    global rdi, rsi, rdx


    rsi = list(reversed(sys.argv))
    rdi = len(sys.argv)
    echo_args()

    exit(0)

if __name__ == "__main__":
    """ Initialize registers (just because)
    """
    rax = ctypes.c_int(64)
    rdi = None
    rsi = None
    stack = []

    main()


