	;; A 64-bit program that displays argv, one per line
	;; On entry, rdi will contain argc and rsi will contain argv

	global main
	extern puts
	section .text


main:				; this is function my_args() in python
	
	push 	rdi		; save registers that puts uses to the stack
	push 	rsi		; save...
	sub 	rsp, 8		; align stack before call

	mov	rdi, [rsi]	; the argument string to display
	call	puts		; print it

	add 	rsp, 8		; restore %rsp to pre-aligned value

	pop	rsi		; restore registers that puts used
	pop	rdi		; restore...

	add	rsi, 8		; point to next argument
	dec	rdi		; count down

	jnz	main		; if not zero,  (ZF not zero), loop


	ret