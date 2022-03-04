#ifndef _SHELL_H
#define _SHELL_H

#include "tokenize.h"

/*
 * Handles a single set of tokens recursively, returns 1 when exiting
 */
int do_cmd(token_t* tokens, state_t* shell_state);

/*
 * Recurs on left and right using do_cmd, and returns 1 when shell is exiting
 */
int do_semicolons(token_t* left, token_t* right, state_t* shell_state);

#endif
