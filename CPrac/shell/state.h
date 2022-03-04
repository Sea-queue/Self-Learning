#ifndef _STATE_H
#define _STATE_H
#include "tokenize.h"

typedef struct state state_t;

//creating a new state struct
state_t* new_state();

//free the given state struct
void state_free(state_t* s);

//return the current state
unsigned int get_state(state_t* s);

//set the state to the given status
void set_state(state_t* s, unsigned int i);

//return the previous commands
token_t* get_prev(state_t* s);

// set the prev field of state_t s to the given token_t
void set_prev(state_t* s, token_t* tokens);

#endif
