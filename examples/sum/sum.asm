;;; 64-bit function that returns the sum of the elements in a floating-point
;;; array. The function has prototype:
;;;	double sum(double[] array, uint64_t length)
;;; Source: http://cs.lmu.edu/~ray/notes/nasmexamples/

	global 	sum
	extern puts
	section	.text

sum:
	;; floating-point arguments are stored in the XMM registers.
	pxor	xmm0, xmm0	; zero-out xmm0
	cmp	rsi, 0		; length = 0 has special case (exit)
	je	done



next:

	addsd	xmm0, [rdi]	; move to next element in array (offset)
	add	rdi, 8		; move to next array element (idx)
	dec	rsi		; count down len(array)
	jnz	next



done:
	;; xmm0 already has return value.
	ret
