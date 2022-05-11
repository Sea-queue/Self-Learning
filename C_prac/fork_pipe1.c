#include <assert.h>
#include <stdio.h>      //perror()
#include <unistd.h>     //fork(); close(); exec(); dup(); pipe()
#include <stdlib.h>     //exit()
#include <fcntl.h>      //open()
#include <sys/wait.h>   // wait()

//$: ls /bin | nl
int main(int argc, char** argv) {
    //Default file descriptors:
    // 0 -> stdin
    // 1 -> stdout
    // 2 -> stderr
    //the pipe system call creates two file descriptors: pick the next two
    //available ints that represents the file descriptors.
    // 3 -> read_fd
    // 4 -> write_fd
    int pipe_fds[2];
    assert(pipe(pipe_fds) == 0);    // returns 0 on success
    int read_fd = pipe_fds[0];
    int write_fd = pipe_fds[1];

    //fork would clone the parent process to child process, meaning:
    //copy the file descriptor status from parent to child, and using
    //pipe to communicate between child and parent.
    int child_pid = fork();

    //in parent
    if (child_pid > 0) {
        // close the read end of the pipe, because we are not using it
        // and in parent we will write to the pipe
        close(read_fd);

        //when close 1, stdout is closed, and 1 is avaible to be reassigned
        if (close(1) == - 1) {
            perror("Error closing stdout");
            exit(1);
        }

        //dup will make a copy of write_fd, say new_fd, and assign the lowest
        //available file descriptor to it which is 1-stdout we just closed(freed)
        //before; and new_fd(aka 1, aka stdout) will point to where write_fd points
        //which is the pipe. Note that write_fd is still 4.
        assert(dup(write_fd) == 1);

        // ls /bin by default calls stdout, and stdout now writes to pipe
        if (execlp("ls", "ls", "/bin", NULL) == -1) {
            perror("Error - execlp failed");
            exit(1);
        }

        /*
            wait isn't necessary because, which process(child or parent) runs
            first, depends on the CPU schedular, if the child(writing) process
            gets run first, since there is nothing in the pipe to read off, the
            child process will be waiting untill parent writes to the pipe.

            if parent runs first, after execute ls /bin, the parent process dies.
            if there /bin is replaced with a file that has infinite loop,
            the parent will never die, once it run out of the time that CPU allocate
            to it, the parent process get suspended, and CPU would let child run
            for certain time, and back to parent, and so on.
         */
    }
    // in child, fork() returns 0 when in child
    else if(child_pid == 0) {
        // close the write end of the pipe
        close(write_fd);

        //when close 0(stdin), 0(stdin) is ready to be reassigned
        if (close(0) == -1) {
            perror("Error closing stdin");
            exit(1);
        }

        // dup copy read_fd to new_fd, and will pick the lowest available int
        // to be the input which is the 0(stdin) we closed(freed) before,
        // now, new_fd(aka 0, aka stdin) points where read_fd points to which is
        // the pipe.
        assert(dup(read_fd) == 0);

        // nl, by default, reads from stdin, and stdin now points to read_fd(the pipe)
        if (execlp("nl", "nl", NULL) == -1) {
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
