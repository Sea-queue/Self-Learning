#include <stdio.h>
#include <stdlib.h>

/*
Any address you can see as programmer of a user-level program is a virtual
address. It's only the OS, through its tricky techniques of virtualizing
memory, that knows where in the physical memory of the machine these
instructions and data values lie. So never forget: if you print out an
address in a program, it's a virtual one, an illusion of how things are
laid out in memory; only the OS (and the hardware) knows the real truth.

When printing out the follow: you can see that code comes first in the
address space, then the heap, and the stack is all the way at the other
end of this large virtual space. All of these addresses are virtual, and
will be translated by the OS and hardware in order to fetch values from
their true physical locations.
 */
int main(int argc, char * argv[]) {
    printf("location of code: %p\n", main);
    printf("location of heap: %p\n", malloc(100e6));
    int x = 3;
    printf("location of stack: %p\n", &x);
    return x;
}
