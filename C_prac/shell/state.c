#include <stdlib.h>
#include <assert.h>

#include "state.h"
#include "tokenize.h"

//main struct of a shell state representing the status of the shell
struct state {
	unsigned int status;  // 0 to exit or 1 stay running
	//do we need to store all the previous commands?
	token_t* prev;	      // storing the previous commands
};


//creating a new state struct
state_t* new_state() {
	state_t* state = (state_t*)malloc(sizeof(state_t));
	state->status = 1;
	token_t* t = new_token();
	state->prev = t;
	return state;
}

//free the given state struct
void state_free(state_t* s) {
	assert(s != NULL);
	free(s->prev);
	free(s);
}

//return the current state
unsigned int get_state(state_t* s) {
	assert(s != NULL);
	return s->status;
}

//set the state to the given status
void set_state(state_t* s, unsigned int i){
	assert(s != NULL);
	s->status = i;
}


//return the previous commands
token_t* get_prev(state_t* s) {
	assert(s != NULL);
	return s->prev;
}

// set previous command
void set_prev(state_t* s, token_t* tokens) {
	assert (s != NULL);
	token_free(s->prev);
	s->prev = tokens;
}
