;;; Original program found at https://gist.github.com/Archenoth/5380671

	section .data
message:		db	'Hello, world!',0x0A ; message and newline
file:			db	'./herpderp'	     ; File to write
length:			equ	$-message	     ; NASM definition pseudo-instruction	

	;;  Write to and create file
	global main

	section .text



main:
	;; 
	;;  sys_open(file, permissions)
	;; 
	mov	rax, 2		; sys_open
	mov	rdi, file	; file


	mov	rsi, 2		; Read/Write permissions
	syscall

	;;  File exists?
	mov	rdx,0
	cmp	rdx,rax
	jle	WR

	;; (except IOError) If read was successful, we'd be in WR
	;;  by now.
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;; 
	;;  Create file
	mov	rax,85		; sys_creat
	syscall			; rax now has a return value in it (hopefully 0)

	;;  File created sucessfully?
	mov	rdx,0
	cmp	rax,rdx
	jle	EX

WR:
	;; globals..(py)
	;;  File descriptor copy
	mov	rbx,rax

	;;  sys_write(stream, message, length)
	mov	rax, 1        	; sys_write
	mov	rdi, rbx        ; ./nope
	mov	rsi, message    ; message address
	mov	rdx, length    	; message string length
	syscall

	mov	rax, 3
	syscall

EX:
	;;  sys_exit(return_code)
	mov	rax, 60        	; sys_exit
	mov	rdi, 0        	; return 0 (success)
	syscall

