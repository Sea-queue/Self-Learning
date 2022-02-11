/* Complete the C version of the driver program for fib. This C code does not 
 * need to compile. */

#include <stdio.h>
#include <stdlib.h>

unsigned long fib(unsigned long num) {
  if (num == 0) {
  	return 0;
  }

  else if (num == 1) {
  	return 1;
  }

  else {
  	return fib(num - 1) + fib(num - 2);
  }
}

int main(int argc, char *argv[]) {
  if (argc != 2 || atol(argv[1]) < 0) {
  	printf("A natural number argument is required\n");
  }
  else {
	long num = atol(argv[1]);
  	printf("passed num is: %ld\n", num);
	printf("%ld\n", fib(num));
  }
  return 0;
}

