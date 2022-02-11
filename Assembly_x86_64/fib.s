# Write the assembly code for main and fib.
.global main

.text
fib:
	enter $0, $0
	
	cmp $1, %rdi
        jl fib_base_0
 	je fib_base_1
	jg fib_else

fib_else:
	dec %rdi
	push %rdi	# push (n-1) to the statck
	call fib
	pop %rdi        # get (n-1) back
	push %rax       # push f(n-1) to the stack
	
	dec %rdi
	call fib
	pop %r12	# get f(n-1) back and store it in %r12
	add %r12, %rax	# store f(n-1) + (n - 2) in %rax
	jmp fib_ret

fib_base_0:
	mov $0, %rax
	jmp fib_ret

fib_base_1:
	mov $1, %rax

fib_ret:
	leave
	ret


main:
	enter $0, $0
	
	movq 8(%rsi), %r12	# move the number to %r12
	mov %rdi, %r13		# move the number of arguments to %r13
	
	# make sure provide only one number
	cmp $2,   %r13
	jl error
	jg error
	
	# make sure the number is positive
	mov %r12, %rdi
	mov $0, %al
	call atol
	mov %rax, %r12
	cmp $0, %r12
	jl  error
	
	mov %r12, %rdi
	call fib

	movq $long_format, %rdi
    	movq %rax, %rsi
    	movb $0, %al
    	call printf
	jmp end

error:
        mov $error_message, %rdi
        mov $0, %al
        call printf

end:
        movq $1, %rax
        leave
        ret
.data

error_message:
	.asciz "A natural number argument is required\n"	

long_format:
	.asciz "%ld\n"	
