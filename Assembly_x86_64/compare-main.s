# Write the assembly code for main

.global main

.text
main:
	enter $0, $0
	mov 8(%rsi),  %r12	# move the first argument to %r12
	mov 16(%rsi), %r13	# move the second argument to %r13
 	
	mov %rdi, %r14
	cmp $3, %r14
	jl error
	jg error
	
		
	# convert first argument to long int	
	mov %r12, %rdi
	mov $0, %al
	call atol
	mov %rax, %r12
	
	# convert the second argument to long int
	mov %r13, %rdi
        mov $0, %al
        call atol
        mov %rax, %r13
	
	# call procided compare function
	mov %r12, %rdi
	mov %r13, %rsi
	mov $0, %al
	call compare
	
	cmp $0, %rax
	jl less
	jg greater
	
 	mov $equal_message, %rdi
	mov $0, %al
	call printf
	jmp end

less:
	mov $less_message, %rdi
        mov $0, %al
        call printf
	jmp end

greater:
	mov $greater_message, %rdi
        mov $0, %al
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

long_format:
	.asciz "%ld\n"

equal_message:
	.asciz "equal\n"

less_message:
	.asciz "less\n"

greater_message:
	.asciz "greater\n"

error_message:
	.asciz "Two arguments required\n"
