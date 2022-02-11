/* Complete the C version of the driver program for compare. This C code does
 * not need to compile. */

#include <stdio.h>

extern long compare(long, long);

int main(int argc, char *argv[]) {
  if (argc != 3) {
      printf("Two arguments required\n");
  }
  else {
      long num1 = atol(argv[1]);
      long num2 = atol(argv[2]);
      if (compare(num1, num2) < 0) {
      	printf("less\n");
      }
      else if (compare(num1, num2) > 0) {
        printf("greater\n");
      }
      else {
        printf("equal\n");
      }
  }
  	
  return 0;
}

