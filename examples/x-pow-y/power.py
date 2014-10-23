import sys, ctypes
"""
Python approximation of power.asm

Returns sys.argv[2] ** sys.argv[3]
"""
raise NotImplementedError("This file isn't done yet.")








def echo_args():             # See function 'echo_args' in echo.asm
    global stack, r12, r13, r14, rdi, rsi
    stack.append(r12) # "push"
    stack.append(r13) # "push"
    stack.append(r14) # "push"
    
    if rdi != 3:      # zflag = 1 if rdi == 3 else 0
        error1()      # if zflag == 0 goto error1

    r12 = rsi


    


    rdi = r12[2]      # rdi = pointer in asm
    eax = int(rdi)    # atoi(rdi) -> eax
    if eax < 0:
        error2()
        r13 = eax     # This was actually r13d in the code (r13[32:])

    rdi = r12[1]      # They're accessing memory locations (pointers)
    eax = int(rdi)    # atoi(rdi) -> eax
    r14 = eax

    eax = 1

def check():
    global r13, r14, eax
    ZF = 0 if r13 & r13 else 1
    if ZF == 0:
        gotit()
    eax *= r14
    r13 -= 1
    check()

def gotit():
    global answer, rdi, rsi, eas, rax
    rdi = answer
    rsi = eax          # no sign extension in this code.
    rax ^= rax         # rax = xor(rax, rax)
    printf()
    done()

def printf(): # extern'd
    print rsi ## Look up args for this




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
    r12 = ctypes.c_int(64)
    r13 = ctypes.c_int(64)
    r14 = ctypes.c_int(64)

    stack = []

    main()


