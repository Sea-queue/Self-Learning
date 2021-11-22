#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("report3.txt", "w");
    fprintf(fpointer, "The difficult part about this assignment is the logic");
    fprintf(fpointer, " of using letters to\nrepresent 11 through 19.");
    fprintf(fpointer, "\nStarting earlier is definitely helpful.\nFully understand");
    fprintf(fpointer, " the hw handout is also helpful too.\n");
    fprintf(fpointer, "Having a piece of paper to try the code I wrote helps to me find");
    fprintf(fpointer, " the bugs.");
    fprintf(fpointer, "\nThis homework helps me to grasp how functions and loop work.");
    fprintf(fpointer, "\nAlso, I have better understanding of base4 and base20 system.");
    fclose(fpointer);
    return 0;
}
