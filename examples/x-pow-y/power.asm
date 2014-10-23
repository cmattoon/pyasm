	;; Source code from http://cs.lmu.edu/~ray/notes/nasmexamples/
	;; A 64-bit command line application to compute x^y
	;; Usage:
	;; 	power x y
	;; x and y are 32-bit integers
	;; rdi = argc
	;; rsi = argv
	
	global main
	extern printf
	extern puts
	extern atoi		; alpha to int (for CLI args)

	section .text

main:
	push	r12		; save callee - save registers
	push 	r13
	push 	r14
	;; by pushing three registers, our stack is already aligned for calls

	cmp 	rdi, 3		; must have exactly two arguments
	jne	error1

	mov 	r12, rsi	; rsi = argv

	;; ecx = count down from the exponent to zero
	;; esi = value of the base
	;; eax = running product

	mov	rdi, [r12+16]	; argv[2]
	call	atoi		; y in eax (return result)
	cmp	eax, 0		; disallow negative exponents
	jl	error2		; jump to error2 if (cmp) was less than 0
	mov	r13d, eax	; store 'y' in r13d [lower 32 bits of r13]

	mov 	rdi, [r12+8]	; x = argv[1]
	call 	atoi		; x in eax
	mov 	r14d, eax	; store 'x' in r14d [lower 32 bits of r14]

	mov	eax, 1		; start with answer = 1

check:

	test	r13d, r13d	; we're counting y down to zero
	jz	gotit		; jump if zero

	imul	eax, r14d	; multiply by x again
	dec	r13d		; count down
	jmp	check		; test again

gotit:				; print report on success

	mov 	rdi, answer	; 
	movsxd	rsi, eax	; move with sign extension -- eax (32) -> rsi(64)
	xor	rax, rax	; zero out rax
	call 	printf
	jmp 	done

error1:				; print error message
	mov	edi, badArgumentCount
	call	puts
	jmp	done

error2:
	mov	edi, negativeExponent
	call puts

done:
	pop	r14
	pop	r13
	pop	r12
	ret

answer:
	db	"%d", 10, 0

badArgumentCount:
	db	"Requires exactly two arguments", 10, 0

negativeExponent:
	db	"The exponent may not be negative", 10, 0