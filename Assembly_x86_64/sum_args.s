# Initialize a running sum as a stack-allocated variable -8(%rbp) to 0.
# You will need to use movq to specify the size of the variable.

# In a loop, convert each argument (remember to skip the program name!) to a
# long integer and add it to the running sum. you will want to use atol

.global main

.text

main:
  # we are using callee-save registers to preserve information when calling printf
  push %r12
  push %r13
  push %r14
  enter $8, $0

  mov %rdi, %r12   # number of arguments
  mov %rsi, %r13   # argument addresses
  mov $0, %r14     # counter
  movq $0, -8(%rbp)

  # testing
  # add $12, -8(%rbp)
  # add $8, -8(%rbp)
  # mov -8(%rbp), %rsi
  # mov $long_format, %rdi
  # mov $0, %al
  # call printf

  mov $sum_prompt, %rdi
  mov $0, %al
  call printf
loop:
  cmp %r12, %r14
  jge loop_end

  # skip the program name
  cmp $0, %r14
  je skip

  # add each argument
  mov (%r13, %r14, 8), %rdi
  mov $0, %al
  call atol
  movq %rax, %rdi
  add %rdi, -8(%rbp)

  skip:
  inc %r14
  jmp loop

loop_end:
  # print the sum of all the arguments
  mov $long_format, %rdi
  movq -8(%rbp), %rsi
  mov $0, %al
  call printf

  leave
  pop %r14
  pop %r13
  pop %r12
  ret

.data

format:
  .asciz "%d: \"%s\"\n"

long_format:
  .asciz "%ld\n"

sum_prompt:
  .asciz "Sum: "
