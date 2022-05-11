#include <assert.h>
#include <stdio.h>      //perror()
#include <unistd.h>     //fork(); close(); exec(); dup(); pipe()
#include <stdlib.h>     //exit()
#include <fcntl.h>      //open()
#include <sys/wait.h>   //wait()

//$: sort < many_words.txt | tail > sorted_tail.txt
int main(int argc, char** agrv) {
    //nl makefile | tail

    char* cmd1[3] = {"nl", "makefile", NULL};
    char* cmd2[2] = {"tail", NULL};

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
                        exit(1);
                }


		//in child_b
		if (child_b == 0) {
			close(read_fd);

			if (close(1) == -1) {
				perror("Error closing stdout");
				exit(1);
			}

			assert(dup(write_fd) == 1);

			//execute command1
			if (execvp(cmd1[0], cmd1) == -1) {
				perror("Error - execvp failed");
				exit(1);
			}
		}

		//in child_a:
			close(write_fd);

			if (close(0) == -1) {
				perror("Error closing stdin");
                        	exit(1);
			}

			assert(dup(read_fd) == 0);

			//execute command2
               	 	if (execvp(cmd2[0], cmd2) == -1) {
                		perror("Error - execvp failed");
                        	exit(1);
                	}
			waitpid(child_b, 0, 0);
	}

	//in parent
	else if (child_a > 0) {
		waitpid(child_a, 0, 0);
	}

	else {
                perror("Error - fork failed");
                exit(1);
        }

	return 0;
}
