## Python translation of create.asm
import os
# section .data
message = "Hello, world!\n"
filename = './herpderp-py'
length = len(message)
fd = None
rax = 0
rbx = 0
rcx = 0
rdx = 0
rsi = 0
rdi = 0

def main():
    global filename, fd, rax, rbx, rdi, rsi
    rax = 2 # Syscall for sys_open(file, permissions). Not needed in python

    try:
        rax = 2 # syscall number. irrelevant here
        rdi = filename

        rsi = 'rw+'
        fd = open(rdi, rsi) # This function is determined by rax

        
        # Set rdx = 0 for comparison
        # Jump if rax (syscall exit code?) had clean exit (no exceptions)
        WR()

    except IOError: 
        """ mov rdx, 0
            cmp rax, rdx
            jle EX
        This code compares rax (return value) to a freshly-zeroed
        rdx register. 'cmp' has the following truth table:
        cmp a, b     ZF    CF
        ---------------------
          a == b      1     0
          a < b       0     1
          a > b       0     0

          So the "jle" instruction jumps if a <= b, or when the return
          value was negative (error)
          """
        fd = open(filename, 'a+')
        rax = 1 if os.path.exists(filename) else -1 # fake syscall return val
        # ;; File created successfully?
        rdx = 0 # mov rdx, 0
        if rax <= rdx:
            EX() 
        
def WR():
    global filename, fd, rax, rbx, rdx, message, length
    rax = fd# If we jumped, rax would be the file pointer
    rbx = rax
    
    # sys_write(stream, message, length)
    rax = 1 # sys_write
    rdi = rbx # File
    rsi = message
    rdx = length

    rdi.writelines(rsi) # rdx not needed in python
    
    rdi.close()
    
def EX():
    # There's a more proper way to illustrate this with dynamic calling. brb.
    print "Exit"
    rdi = 0 # code
    exit(rdi)

main()
