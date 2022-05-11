#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "tokenize.h"

// token structure that stores acctual tokens and the amount of tokens.
struct token {
        char** token_list;      // array of tokens
        unsigned int size;      // the size of the token_list
        unsigned int capacity;  // the capacity of the token_list
};


// create new token struct
token_t* new_token() {
        token_t* t = (token_t*) malloc(sizeof(token_t));
        char** tokens = (char**)malloc(INITIAL_CAPACITY * sizeof(char*));
        t->token_list = tokens;
        t->size = 0;
        t->capacity = INITIAL_CAPACITY;
        return t;
}

// free the given token struct
void token_free(token_t* t) {
  assert(t != NULL);

  for (int i = 0; i < t->size; i += 1) {
    free(t->token_list[i]);
  }

  free(t->token_list);
  free(t);
}



// print token contents on one line 
void print_tokens(token_t* tokens) {
	for (int i = 0; i < tokens->size; i++) {
		printf("%s ", get_token(tokens, i));
	}
	printf("\n");
}

//add the given string to the array of strings,
void add_tokens(token_t *token, const char* to_add) {
        assert((token != NULL) && (to_add != NULL));

        if (token->size >= token->capacity) {
                token->capacity *= GROW_FACTOR;
                token->token_list = realloc(token->token_list, token->capacity * sizeof(char*));
        }
	token->token_list[token->size] = (char*)malloc(sizeof(char) * (strlen(to_add) + 1));
	strcpy(token->token_list[token->size], to_add);
	token->size += 1;
}

// copy source and return the copy
token_t* copy_tokens(token_t* source) {
        token_t* copy = new_token();
        for (int i = 0; i < source->size; i++) {
          add_tokens(copy, get_token(source, i));
        }
        return copy;
}

// get the token of given index in the given token struct
const char* get_token(token_t* t, unsigned int idx) {
        assert(t != NULL);
        assert(idx < t->size);
        return t->token_list[idx];
}


// get the size of the given token
unsigned int token_size(token_t* t) {
        assert(t != NULL);
        return t->size;
}

// is the given character a special character? (, ), <, >, ;, or |
int is_special(char ch) {
  return (ch == '(' || ch == ')' || ch == '<' || ch == '>' || ch == ';' || ch == '|');
}


// scans for first instance of a semicolon
// return -1 if not found
int first_cmd_symbol(token_t* tokens, char cmd) {
  for (int i = 0; i < token_size(tokens); i++) {
  	if (strlen(get_token(tokens, i)) == 1 
			&& get_token(tokens, i)[0] == cmd) {
	  return i;
	}	
  }
  return -1;
}

// return a copy of the tokens from the specified range [start, end - 1]
token_t* partition_range(token_t* tokens, int start, int end) {
        token_t* output = new_token();
        assert(start < end);
        assert(token_size(tokens) >= end);
        for (int i = start; i < end; i++) {
                add_tokens(output, get_token(tokens, i));
        }
        return output;
}

// is the given character whitespace?
int is_whitespace(char ch) {
  return (ch == ' ' || ch == '\t');
}

//Read the next letter as a string from the input into the output.
int read_letter_string(const char *input, char *output) {
  int i = 0;
  // while we have input and the character is a digit,
  while (input[i] != '\0' && !(is_special(input[i]) || is_whitespace(input[i]))) {
    output[i] = input[i]; // copy character to output buffer
    ++i;
  }
  output[i] = '\0'; // add the terminating byte

  return i; // return the length of the string
}


// adding everthing before interact another double qoute
int read_everything(const char* input, char* output) {
	int i = 0;

	while (input[i] != '\0' && input[i] != '"') {
		output[i] = input[i];
		++i;
	}

	output[i] = '\0';
	return i;
}	


// takes a string (char*) and returns a list of tokens
token_t* tokenize_func(char* input_str) {
    token_t* t = new_token();
    char buf[256];      // temp buffer
    int i = 0;  // current position in string
	
    int in_str = 0;  //False 
    // while the end of string is not reached
    while (input_str[i] != '\0') {
      if (input_str[i] == '"') {
      	if (in_str == 0) {
		in_str = 1;
	}
	else {
		in_str = 0;
	}
	i++;
	continue;
      }

      if (in_str == 1) {
	i += read_everything(&input_str[i], buf);
      	add_tokens(t, buf);
	continue;
      }

      else {
      	// first check if the current char is a letter
      	if (!(is_special(input_str[i]) || is_whitespace(input_str[i]))) {

        	// read the integer from the output AND
        	// advance the current position by the length of the string
        	i += read_letter_string(&input_str[i], buf);
        	add_tokens(t, buf);
		continue; // skip the rest of this iteration
      	}

      	// here, current character is not a number or a letter
      	if (is_special(input_str[i])) {
      		char st[2];
		st[0] = input_str[i];
		st[1] = '\0';
		add_tokens(t, st);
      	} 
      	
	++i; // advance to the next character
   	}
      }
      return t;
}
