	;; This is a 64-bit assembly function that returns the maximum value of its three
	;; parameters and has the signature:
	;; 	int64_t maxofthree(int64_t x, int64_t y, int64_t z)
	;; The parameters are passed in as rdi, rsi, rdx.
	;; The return value goes in rax
	global maxofthree
	section .text
	;; rdi = sys.argv[1]
	;; rsi = sys.argv[2]
	;; rdx = sys.argv[3]
	
maxofthree:
	;; No need to init globals in asm
	mov	rax, rdi	; rax = rdi

	cmp	rax, rsi	; if rax < rsi:
	cmovl	rax, rsi	;     rax = rsi

	cmp 	rax, rdx	; if rax < rdx:
	cmovl	rax, rdx	;     rax = rdx

	ret			; return rax