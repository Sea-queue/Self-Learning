# Write the assembly code for array_max
.global array_max

.text
array_max:
	enter $0, $0
	mov %rdi, %r12		# move the first argument into %r12 
	mov (%rsi), %r13	# stores the first element into %r13
	mov $0, %r14		# stores the index i
	mov $0, %r15		# stores the max

loop:
	cmpq %r12, %r14
	jge loop_end
		
	cmp %r13, %r15
	jge update_r13		# smaller than the current max, ignore
	jmp update_r15		

update_r13:
	inc %r14
	mov (%rsi, %r14, 8), %r13
	jmp loop

update_r15:
	inc %r14
	mov %r13, %r15          # record the new max
        mov (%rsi, %r14, 8), %r13
	jmp loop

loop_end:
	mov %r15, %rax
	leave
	ret


.data
long_format:
	.asciz "%ld\n"


