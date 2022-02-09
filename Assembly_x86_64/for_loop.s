# !> print an array of numbers in a "for loop"

.global main

.text
main:
    enter $0, $0

    # numbers -> %r12
    # i -> %r13
    mov $numbers, %r12
    mov $0, %r13            # i = 0

loop:
    cmpq $8, %r13           # i < 8
    jge  loop_end           # end the loop

    mov $long_format, %rdi
    mov (%r12, %r13, 8), %rsi
    mov $0, %al
    call printf

    incq %r13
    jmp  loop


loop_end:
    mov $0, %rax
    leave
    ret


.data
numbers:
    .quad 1, 2, 3, 4, 5, 6, 7, 8

long_format:
    .asciz "%ld\n"
