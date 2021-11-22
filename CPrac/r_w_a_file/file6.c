#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("report6.txt", "w");
    fprintf(fpointer, "The first difficulty is sorting every point by their polar angle --\n");
    fprintf(fpointer, "Knowing how to calculate their polar angle and then use bubble sort.\n");
    fprintf(fpointer, "I learned how to think like a computer, narrowing the possibilities to pinpoint\n");
    fprintf(fpointer, "the mistakes I made.\n");
    fprintf(fpointer, "The second difficulty is using stack to select the points I need.\n");
    fprintf(fpointer, "I learned how to use push and pop.\n");
    fprintf(fpointer, "The third difficulty is the logic of selecting the right points.\n");
    fprintf(fpointer, "It took me a while to create two if statements to get ride of points I\n");
    fprintf(fpointer, "I don't need.\n");
    fprintf(fpointer, "I got more confident on thinking about logic with papers and pens.\n");
}
