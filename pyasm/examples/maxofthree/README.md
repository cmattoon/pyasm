To compile & run:
    nasm -felf64 maxofthree.asm && gcc callmaxofthree.c maxofthree.o && ./a.out

Compare with:
    python maxofthree.py


This example creates a function in assembly that is then called from a C 
program. The function takes three 64-bit integers (int64_t) as parameters
and outputs the largest one. 