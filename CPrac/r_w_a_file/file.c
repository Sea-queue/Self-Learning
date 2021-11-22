#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("cs240:\employees.txt", "w");
    fprintf(fpointer, "Jim, professor\nSeaqueue, TA\n");
    fclose(fpointer);
    return 0;
}
