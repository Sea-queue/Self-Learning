#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include "tokenize.h"
#include <assert.h>
#include "state.h"
#include "shell.h"
#include "state.h"

//maximum size of a single line.
int MAX_SIZE = 256;


// generates a list of tokens with given tokens and size
char** generate_args(token_t* tokens, int command_size) {
	 //const char* myargv[command_size + 1];
	 char** myargv = (char**)malloc(sizeof(char*) * command_size + 1);
         for (int i = 0; i < command_size; i += 1) {
    		 myargv[i] = malloc(sizeof(char*) * (strlen(get_token(tokens,i)) + 1));
                 const char* curr_tok = get_token(tokens, i);
                 if (strcmp(curr_tok, "\n") == 0 || strcmp(curr_tok, " ") == 0) {
   	              continue;
                 }
                 strcpy(myargv[i], curr_tok);
                 assert(myargv[i][strlen(myargv[i]) - 1] != '\n');
         }
         myargv[command_size] = NULL;

	return myargv;
}

// if error reading source, return -1, otherwise return 0.
int read_source(const char* filename, state_t* sh_state) {
	char buf[MAX_SIZE];
	FILE* fd = fopen(filename, "r");
	if (fd == NULL) {
	  return -1;
	}

	// token_t* prev_temp =

	// return -1 if file not found
	// tokenize each line and feed it to do_cmd
	while (fgets(buf, MAX_SIZE, fd) != NULL) {
	  buf[strcspn(buf, "\n")] = 0;
	  token_t* line = tokenize_func(buf);
	  do_cmd(line, sh_state);
	}
	return 0;
}



//executes the commands without redireciton or pipe
int command_basic(token_t* tokens, state_t* shell_state) {
		int command_size = token_size(tokens);
	        // assert(command_size >= 1);
		if (command_size < 1) {
		  return 0;
		}

        	//exit the program when user types " exit "
	        if (command_size == 1 && strcmp(get_token(tokens, 0), "exit") == 0) {
		  set_state(shell_state, 0);
        	  return 1;
       	 	}

		//TODO: implement the built-in commands
		// begin my work on builtins
                if (command_size == 1 && strcmp(get_token(tokens, 0), "help") == 0) {
                  printf("\tcd <destination> -- moves current working directory to destination\n\t"
		                  "source <script> -- executes script as if contents of script were to be entered\n\t"
                                  "\tline by line into the shell\n\t"
                                  "prev -- prints previous command and executes it again\n\t"
                                  "help -- explanation of builtin commands\n\t"
				  "exit -- closes shell program\n");
                  return 0;
                }

		if (command_size == 1 && strcmp(get_token(tokens, 0), "prev") == 0) {
			print_tokens(get_prev(shell_state));
			return do_cmd(copy_tokens(get_prev(shell_state)), shell_state);
		}

		//TODO: Add in cd and source

		if (strcmp(get_token(tokens, 0), "cd") == 0) {
			if (command_size > 2 || command_size == 1) {
				printf("cd takes two commands in format: shell$ cd <destination>\n");
				// return 0;
			} else if (chdir(get_token(tokens, 1)) != 0) {
				perror("invalid directory");
			}
			return 0;
		}
		if (strcmp(get_token(tokens, 0), "source") == 0) {
			if (command_size > 2 || command_size == 1) {
				printf("source takes two commands in format: shell$ source <script>\n");
			} else if (read_source(get_token(tokens, 1), shell_state) != 0) {
				perror("error reading source file");
			}
			return 0;
		}


		int fork1_id;
        	int fork1 = fork();
        	if (fork1 == 0) {
                	fork1_id = getpid();

			char** myargv = generate_args(tokens, command_size);
			if (execvp(myargv[0], myargv) == -1) {
                        	printf("No such file or directory\n");
                        	exit(1);
                	}
			_exit(0);
        	}
        	waitpid(fork1, &fork1_id, 0);

	return 0;
}


//1: only one redirection, 0: more than one redirection
int base_redirection(token_t* tokens) {
	int accu = 0;  //keeps track of the amount of redirections
	for (int i = 0; i < token_size(tokens); i += 1) {
		if (accu > 1) { return 0; }
		if (strcmp(get_token(tokens, i), "<") == 0 ||
		    strcmp(get_token(tokens, i), ">") == 0) {
			accu += 1;
		}
	}
	return 1;
}

//returns 1 if tokens contains "<" or ">", otherwise returns 0
int has_redirection(token_t* tokens) {
        for (int i = 0; i < token_size(tokens); i += 1) {
                if (strcmp(get_token(tokens, i), "<") == 0 ||
                    strcmp(get_token(tokens, i), ">") == 0) {
                        // "<", ">"being the first element should be invalid
                        return i;
                }
        }
        return 0;
}

//executes the commands that contains redirection without pipe
int command_redirection(token_t* tokens, state_t* shell_state) {
 	//cmd < cmd > cmd > file

	pid_t child = fork();

	if (child == -1) {
                perror("Error - fork failed");
                _exit(1);
        }

	//in child
	if (child == 0) {
		const char* file_name = get_token(tokens, token_size(tokens) - 1);

                //0 represents "<", 1 represents ">"
                int redirection = 0;
                for (int i = token_size(tokens) - 1; i >= 0; i -= 1) {
                        if (strcmp(get_token(tokens, i), "<") == 0) {
                                redirection = 0;
                                break;
                        }
                        else if (strcmp(get_token(tokens, i), ">") == 0) {
                                redirection = 1;
                                break;
                        }
                }

                //printf("redirection: %d\n", redirection);

                if (redirection == 0) {
                        if (close(0) == -1) {
                                perror("Error closing stdin");
                                _exit(1);
                        }

                        int fd = open(file_name, O_RDONLY);
                        if (fd == - 1) {
				printf("File not found");
			}
			assert(fd == 0);
                }

                if (redirection == 1) {
                        if (close(1) == -1) {
                                perror("Error closing stdout");
                                _exit(1);
                        }

                        int fd = open(file_name, O_WRONLY | O_CREAT | O_TRUNC, 0644);
                        assert(fd = 1);
                }

		//more than one redirections:  sort < a.txt > b.txt
        	if (base_redirection(tokens) == 0) {
			// recur = 1;
			token_t* left = partition_range(tokens, 0, token_size(tokens) - 2);
			left = partition_range(tokens, 0, token_size(tokens) - 2);

			command_redirection(left, shell_state);
			_exit(0);
		} else {
			int command_size = has_redirection(tokens);
                	char** myargv = generate_args(tokens, command_size);
                	if(execvp(myargv[0], myargv) == -1) {
                		perror("Error - execvp failed");
                		_exit(1);
                	}
		}

	}

	//in parent
	else if (child > 0) {
		waitpid(child, 0, 0);
	}

	return 1;
}


//executes the commands that contains pipe
int command_pipe(token_t* tokens, state_t* shell_state) {

	//e.g.: shuf -i 1-10 | sort -n | tail -5
	int first_pipe = first_cmd_symbol(tokens, '|');
	token_t* command1 = partition_range(tokens, 0, first_pipe);
	token_t* command2 = partition_range(tokens, first_pipe + 1, token_size(tokens));

	pid_t child_a = fork();

        //in child_a
        if (child_a == 0) {
		int pipe_fds[2];

		//returns 0 on success
		assert(pipe(pipe_fds) == 0);
		int read_fd = pipe_fds[0];
		int write_fd = pipe_fds[1];

		pid_t child_b = fork();

		if (child_b == -1) {
                        perror("Error - fork failed");
                        _exit(1);
                }


		//in child_b
		if (child_b == 0) {
			close(read_fd);

			if (close(1) == -1) {
				perror("Error closing stdout");
				_exit(1);
			}

			assert(dup(write_fd) == 1);
			token_t* left = partition_range(tokens, 0, first_pipe);
			do_cmd(left, shell_state);
			_exit(1);
		}
		//in child_a:
		close(write_fd);

		if (close(0) == -1) {
			perror("Error closing stdin");
                       	_exit(1);
		}

		assert(dup(read_fd) == 0);

		token_t* right = partition_range(tokens, first_pipe + 1, token_size(tokens));
		do_cmd(right, shell_state);

		waitpid(child_b, 0, 0);
		_exit(1);
	}

	//in parent
	else if (child_a > 0) {
		waitpid(child_a, 0, 0);
	}

	else {
                perror("Error - fork failed");
                _exit(1);
        }

	return 1;
}


//returns 1 if tokens contains "|", otherwise returns 0
int has_pipe(token_t* tokens) {
        for (int i = 0; i < token_size(tokens); i += 1) {
                if (strcmp(get_token(tokens, i), "|") == 0) {
                        return 1;
                }
        }
        return 0;
}


// recursively parse through the tokens and executes the command
int do_cmd(token_t* tokens, state_t* shell_state) {
	if (get_state(shell_state) == 0) {
		token_free(tokens);
		// state_free(shell_state);
		return 1;
	}

	int mid = first_cmd_symbol(tokens, ';');
	int command_value = 0;

	if (mid == -1 || mid == token_size(tokens) - 1) {
		// execute without semicolon

		//condition one: without pipe and redirection
		if (has_redirection(tokens) == 0 && has_pipe(tokens) == 0) {
			//printf("in basic\n");
			command_value = command_basic(tokens, shell_state);
		}

		//condition two: with rediction
		else if(has_pipe(tokens) == 0 && has_redirection(tokens) > 0) {
			//printf("in redirection\n");
			command_value = command_redirection(tokens, shell_state);
		}

		//condition three: with pipe
		else if(has_pipe(tokens) > 0) {
			//printf("in pipe\n");
			command_value = command_pipe(tokens, shell_state);
		}

		else {
			printf("invalid command: should not reach here!");
		}

	} else if (mid == 0) {
		printf("syntax error: near unexpected token \';\'");
	} else {
		token_t* left = partition_range(tokens, 0, mid);
		token_t* right = partition_range(tokens, mid + 1, token_size(tokens));
		if (do_semicolons(left, right, shell_state) == 1) {
			token_free(tokens);
			return 1;
		}

	}
	if (!(token_size(tokens) == 1 && strcmp(get_token(tokens, 0), "prev") == 0)) {
	  set_prev(shell_state, copy_tokens(tokens));
	}
	//set_prev(shell_state, copy_tokens(tokens));
	token_free(tokens);
	// do not free child tokens, and do not free shell_state, we let that be freed by caller (main loop)
	return command_value;
}

int do_semicolons(token_t* left, token_t* right, state_t* shell_state) {

	// forking child A
	pid_t child = fork();
	int child_pid;
	if (child == -1) {
		perror("Error - fork failed");
		_exit(1);
	}

	if (child == 0) {
		child_pid = getpid();
		// in child
		if (do_cmd(left, shell_state) == 1) {
			// exit
			// token_free(right); // only need to free right once
			set_state(shell_state, 0);
			_exit(1);
		}
		_exit(0);
	}
	// in parent
	waitpid(child, &child_pid, 0);


	if (WIFEXITED(child_pid) && WEXITSTATUS(child_pid) == 1) {
		token_free(right); // free right token, hasn't gotten there yet
                set_state(shell_state, 0);
        	return 1;
	}

	// forking child B
	child = fork();
	if (child == -1) {
           perror("Error - fork failed");
           _exit(1);
        }
	if (child == 0) {
                child_pid = getpid();
                // in child
                if (do_cmd(right, shell_state) == 1) {
                        // exit
			// don't need to free left, as do_cmd has already freed left
			//set_state(shell_state, 0);
			_exit(1);
                }
                _exit(0);
        }

	// in parent
        waitpid(child, &child_pid, 0);

	if (WIFEXITED(child_pid) && WEXITSTATUS(child_pid) == 1) {
                set_state(shell_state, 0);
                return 1;
        }
	return 0;
}




//this is a simple shell program that takes in commands and execute it
int main(int argc, char **argv) {
    //start the shell
    printf("%s\n", "Welcome to mini-shell");

    //initial variables
    char command[MAX_SIZE];
    state_t* state = new_state();
    pid_t fork1;
    int fork1_id;

    //main while loop
    while(get_state(state) == 1) {
	printf("%s", "shell $ ");
	if (fgets(command, MAX_SIZE, stdin) == NULL) {
	  printf("\n");
	  set_state(state, 0);
	  continue;
	}

	// removing trailing newline
	command[strcspn(command, "\n")] = 0;

	token_t* t1 = tokenize_func(command);

	// if no tokens here, just continue
	if (token_size(t1) < 1) {
	  continue;
	}

	// this is where we should call our execute command function
	// recursively
	do_cmd(t1, state);
    }
    state_free(state);
    // on normal execution, the user only gets here when they type "exit"
    printf("Bye bye.\n");
    return 0;
}
