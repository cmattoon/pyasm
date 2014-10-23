This function prints out the command line arguments, one per line.

Compiled with:
	 _$ felf64 echo.asm && gcc echo.o
	 

_$ ./a.out first second
./a.out
first
second

_$ python my_args.py first second
my_args.py
first
second


There's a bit of deviation from what's *actually* going on because of the stack alignment, but I think the following points are notable:
 * the literal meaning of the JNZ instruction. I believe this is obtained from the ZF flag that could be set during DEC.
 * as far as I understand, the 'add rsi, 8' instruction on line shifts the argv, but I'm not exactly clear on how.
 * the way ASM counts down (dec rdi), rather than up (for i in range(...))
