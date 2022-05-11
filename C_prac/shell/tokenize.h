#ifndef _TOKENIZE_H
#define _TOKENIZE_H

typedef struct token token_t;

/*
 * Takes in a string representing a series of arguments.
 * Produces an array of strings representing each whitespace
 * separated token of original string.
 * */
token_t* new_token();
token_t* tokenize_func(char* input_str);
const char* get_token(token_t* t, unsigned int idx);
unsigned int token_size(token_t* t);

/*
 * Given a token object, free it and all the memory
 * it is taking up.
 */
void token_free(token_t* t);


/*
 * Prints each individual tokens spaced out on one line
 */
void print_tokens(token_t* tokens);

/*
 * Given a token, what is the index of the first semicolon character?
 * if not found, return -1. 
 */
int first_cmd_symbol(token_t* t, char cmd);


/*
 * Return a copy of the given tokens range from [start, end - 1]
 */
token_t* partition_range(token_t* tokens, int start, int end);

/*
 * Returns a copy of the given token_t source object.
 */
token_t* copy_tokens(token_t* source);

#define INITIAL_CAPACITY 2
#define GROW_FACTOR 2

#endif
