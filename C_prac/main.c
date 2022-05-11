#include <stdio.h>
#include <ctype.h> //for the built in funtion isalnum() in isAlphanumeric()
#include "math_functions.c"

//If the functions are NOT static, it causes duplicate symbol error when
//compiling them together.

//the entry point to test syntax and funtions:
int main() {
   //calling isAlphanumeric
   printf("is alphanumeric?\n");
   isAlphanumeric();
   printf("\n");

   //calling power
   printf("power function: raise 2 and -3\n");
   for (int i = 0; i < 10; ++i) {
     printf("%d %d %d\n", i, power(2, i), power(-3, i));
   }
   printf("\n");


   //calling calculator
   printf("calculator:\n");
   //calculator();
   printf("\n");

}
