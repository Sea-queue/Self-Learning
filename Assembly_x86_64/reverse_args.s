# In the first loop, push each argument's address onto the stack.
# Again, skip the program name.

# Once all arguments have been pushed, in the second loop, pop each argument
# and print it, adding a space after it


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

loop1:
  cmp %r12, %r14
  jge loop1_end

  cmp $0, %r14
  je skip

  # push each argument's address onto the stack
  add $8, %r13
  push %r13

  # testing
  #mov $long_format, %rdi
  #mov %r13, %rsi
  #mov $0, %al
  #call printf
  #mov $space, %rdi
  #mov $0, %al
  #call printf

  skip:
  inc %r14
  jmp loop1

loop1_end:

loop2:
  cmp $1, %r14
  je loop2_end

  # pop the value at the top of the stack
  pop %rdi
  mov (%rdi), %rdi
  mov $0, %al
  call atol
  movq %rax, %rsi
  mov $long_format, %rdi
  mov $0, %al
  call printf

  mov $space, %rdi
  mov $0, %al
  call printf

  dec %r14
  jmp loop2

loop2_end:
  mov $new_line, %rdi
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
  .asciz "%ld"

space:
  .asciz " "

new_line:
  .asciz "\n"
