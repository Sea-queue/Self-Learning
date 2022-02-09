#
# Usage: ./calculator <op> <arg1> <arg2>
#

# Make `main` accessible outside of this module
.global main

# Start of the code section
.text

# int main(int argc, char argv[][])
main:
  # Function prologue
  enter $0, $0

  # Variable mappings:
  # op -> %r12
  # arg1 -> %r13
  # arg2 -> %r14
  movq 8(%rsi), %r12  # op = argv[1]
  movq 16(%rsi), %r13 # arg1 = argv[2]
  movq 24(%rsi), %r14 # arg2 = argv[3]

  	# Hint: Convert 1st operand to long int
	mov %r13, %rdi
	mov $0, %al
	call atol
	movq %rax, %r13
	
	# Hint: Convert 2nd operand to long int
	mov %r14, %rdi
	mov $0, %al
	call atol
	movq %rax, %r14

  	# Hint: Copy the first char of op into an 8-bit register
  	# i.e., op_char = op[0] 
	movb 0(%r12), %r12b
	
	
  	# if (op_char == '+')
	# 1: ascii 2:cmpb $'+', (%rdx) 3: hex 
	cmpb $43, %r12b
	je adding
	
	# if (op_char == '-')
	cmpb $'-', %r12b
	je subtracting

	# if (op_char == '*')
	cmpb $'*', %r12b
	je multiplying
	
	# if (op_chart == '/')
	cmpb $'/', %r12b
	je dividing
	
	# else print error; return 1 from main
	mov $error_message, %rdi
	mov $0, %al
	call printf
	mov $1, %rax 
	jmp end

	adding:
		add %r13, %r14
		mov $0, %al
		mov $format, %rdi
		mov %r14, %rsi
		call printf
 	jmp end	
	
	subtracting:
		sub %r14, %r13
		mov $0, %al
		mov $format, %rdi
		mov %r13, %rsi
		call printf
	jmp end

	multiplying:
		imul %r13, %r14
		mov $0, %al
		mov $format, %rdi
		mov %r14, %rsi
		call printf
	jmp end

	dividing:
		movq %r13, %rax
		cqo
		idiv %r14
		mov $format, %rdi
		mov %rax, %rsi
		mov $0, %al
		call printf 

	end:	
		
  # Function epilogue
  leave
  ret


# Start of the data section
.data

format:
	.asciz "%ld\n"

error_message:
	.asciz "Unknown operation\n"
