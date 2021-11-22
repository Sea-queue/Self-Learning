#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("report4.txt", "w");
    fprintf(fpointer, "The difficult part about this assignment is making sure ");
    fprintf(fpointer, " I understand the truth \ntable of adder. Also trying to use");
    fprintf(fpointer, " as few as boolean to implement the table is hard.\n");
    fprintf(fpointer, "As always, read the hw handout couple times to fully understand");
    fprintf(fpointer, " the homework is\nthe first step.\nHaving a piece of paper to try the code I wrote helps to me find");
    fprintf(fpointer, " the bugs.");
    fprintf(fpointer, "\nThis homework helps me to understand how functions and main() work together.");
    fprintf(fpointer, "\nAlso, it is one more practice so it helps in general feeling of coding.");
    fclose(fpointer);
    return 0;
}
