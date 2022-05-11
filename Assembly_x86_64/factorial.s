# !> Three versions of factorial in assembly

.global main
.text

# Assembly Design Recipe

# 1. Signature / purpose
# long fact(long n)  Computes the nth factorial

# 2. Pseudocode
# long fact(long n) {
#   if (n < 2)
#       return 1;
#   else
#       temp = fact(n - 1)
#       return n * temp;
# }

# 3. Variable mappings
# n -> %rdi -> %r12
# temp -> %rax

# Version 1: callee-save register
fact1:
    # prologue
    pushq %r12      # push 8 bytes
    enter $8, $0    # $8: allocate 8 bytes right after the address of %rbp
                    # $0: the offset in bytes with the address before the %rbp

    # Body
    # if (n < 2)
    cmpq $2, %rdi
    jge  fact1_else

    # return 1
    movq $1, %rax
    jmp fact1_ret

fact1_else:
    # else
    movq %rdi, %r12
    subq $1, %rdi
    call fact1
    # temp = fact(n-1);
    # return n * temp;
    imulq %r12, %rax

fact1_ret:
    leave
    popq %r12
    ret


# Version 2: Using local variables in the stack frame
# n -> %rdi -> -8(%rbp)
# temp -> %rax
fact2:
    # prologue
	enter $16, $0      # allocate 8 bytes + 8 bytes to align rsp

    # Body
    # if (n < 2)
    cmp $2, %rdi
    jge fact2_else

    # return 1
    movq $1, %rax
    jmp  fact2_ret

fact2_else:
    # else
    movq %rdi, -8(%rbp)
    subq $1, %rdi
    call fact2
    # temp = fact2(n - 1);
    # return n * temp;
    imulq -8(%rbp), %rax

fact2_ret:
    leave
    ret


# Version3: Unsing a caller-save register
# n -> %r10
fact3:
    # prologue
    enter $0, $0

    # Body
    # if (n < 2)
    cmpq $2, %rdi
    jge  fact3_else

    # return 1
    movq $1, %rax
    jmp  fact3_ret

fact3_else:
    # else
    mov  %rdi, %r10
    subq $1, %rdi

    # push and pop actually does nothing just moved data back and forth??
    pushq %r10   # push twice to align the stack pointer
    pushq %r10
    call fact3
    # temp = fact3(n - 1)
    # return n * temp;
    popq  %r10
    popq  %r10
    imulq %r10, %rax

fact3_ret:
    leave
    ret



# int main(int argc, char *argv[])
# tmp -> %rax
main:
    enter $0, $0

    #tmp = fact(5)
    movq $5, %rdi
    call fact1

    # printf("%ld\n", tmp)
    movq $long_format, %rdi
    movq %rax, %rsi
    movb $0, %al
    call printf

    # why have a separet return value???
    # return 0
    movq $0, %rax
    leave
    ret

.data
long_format:
    .asciz "%ld\n"
