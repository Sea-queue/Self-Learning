#include <stdio.h>
#include <stdlib.h>
#include "tokenize.h"
#include <unistd.h>

int main(int argc, char **argv) {
  // max input is 256 chars
  char* text = malloc(sizeof(char) * 256);

  // read input from stdin
  fgets(text, 256, stdin);

  
  token_t* list = tokenize_func(text);
  int i = 0;
  for (i = 0; i < token_size(list); i++) {
    printf("%s\n", get_token(list, i));
  }

  // freeing all of the dynamically allocated memory
  token_free(list);
  free(text);
  return 0;
}
