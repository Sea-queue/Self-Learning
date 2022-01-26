#include <stdio.h>

 // Pointer Operator:
 // & (ampersand): "Address of"
 // * : "value at address"

int main () {

    int i = 3;
    /*
     the above declaration tells C compiler to:
     (a): Reserve space in memory to hold the integer value
     (b): Associate the name i with this memory location.
     (c): Store the value 3 at this location.

            i       --> location name
         (  3  )    --> value at location
          65524      --> location number

     Note: location number is different every time, the important point is
           i's address in memory is a number.
     */

     // %u: for printing unsigned integer
     printf("Address of i = %u \n", &i);
     printf("Value of i = %d \n", i);
     printf("Value of i = %d \n", *(&i));

     /*
      Note that *(&i)  is the same as i

      The expression &i gives the address of the variable i. This address can be
      collected in a variable by saying:

      int *j;

      j = &i;

      j is not an ordinary variable like any other variable. It contains the
      address of other variable. The declaration tells the compiler that j will
      be used to store the address of an integer value. In other words j points
      to an integer. Since j is a variable, the compiler must provide it space
      in the memory:

            i                 j
          ( 3 )           ( 65524 )
          65524             65522


      char *ch;
      float *flo;
      */


      int *j;
      j = &i;

      printf("\nAddress of i = %u \n", &i);
      printf("Address of i = %u \n", j);
      printf("Address of j = %u \n", &j);
      printf("Value of j = %u \n", j);
      printf("Value of i = %d \n", i);
      printf("Value of i = %d \n", *(j));
      printf("Value of i = %d \n", *(&i));
      printf("Value of i = %d \n", *(*(&j)));

      /*
       The concept of pointers can be further extended. Pointer is a variable
       that contains address of another variable which could be another pointer.

               i                 j                  k
             ( 3 )           ( 65524 )          ( 65522 )
             65524             65522              65520
       */

       int **k;
       k = &j;
       printf("\nAddress of i = %u \n", *(k));
       printf("Value of i = %d \n", *(*k));
}
