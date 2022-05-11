#include <assert.h>
#include <stdio.h>      //perror()
#include <unistd.h>     //fork(); close(); exec(); dup(); pipe()
#include <stdlib.h>     //exit()
#include <fcntl.h>      //open()
#include <sys/wait.h>   //wait()

//$: sort < many_words.txt | tail > sorted_tail.txt
int main(int argc, char** agrv) {
    //store output of "sort < many_words.txt | tail" into sorted_tail.txt
    int final_fd = open("sorted_tail.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    int pipe_fds[2];
    assert(pipe(pipe_fds) == 0);
    int read_fd = pipe_fds[0];
    int write_fd = pipe_fds[1];

    int child_pid = fork();

    //in parent: write into pipe
    if (child_pid > 0) {
        close(read_fd);

        //close stdout, free 1(stdout) to be reassigned
        if (close(1) == -1) {
            perror("Error - closing stdout");
            exit(1);
        }
        //copy a new file descriptor new_fd which is the lowest available
        //1-stdout in this case, points to where write_fd points which is pipe
        //write end, note write_fd is still 4.
        assert(dup(write_fd) == 1);

        //close stdin, free 0(stdin) to be reassigned
        if (close(0) == -1) {
            perror("Error - closing stdin");
            exit(1);
        }
        //takes 0(stdin); so now 0 poits to "many_words.txt"
        int input_fd = open("many_words.txt", O_RDONLY);
        assert(input_fd == 0);

        //read from the stdin(aka 0, aka input_fd), and write to stdout(aka 1, aka pipe)
        if (execlp("sort", "sort", NULL) == -1) {
            perror("Error - execlp failed");
            exit(1);
        }
    }

    //in child
    else if (child_pid == 0) {
        close(write_fd);

        if (close(0) == -1) {
            perror("Error closing stdin");
            exit(1);
        }

        //copy read_fd to new_fd which takes the lowest file descriptor available
        //which is 0 we freed up there, and points to where read_fd points which is
        // in the pipe
        assert(dup(read_fd) == 0);

        if (close(1) == -1) {
            perror("Error closing stdout");
            exit(1);
        }

        //copy final_fd to new_fd which takes the lowest file descriptor available
        //which is 1 we freed up there, and points to where final_fd points
        assert(dup(final_fd) == 1);

        if(execlp("tail", "tail", NULL) == -1) {
            perror("Error - execlp failed");
            exit(1);
        }
    }
    else {
        perror("Error - fork failed");
        exit(1);
    }
    return 0;
}
