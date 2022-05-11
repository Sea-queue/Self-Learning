#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("cs240:\employees.txt", "a");
    fprintf(fpointer, "overridden");
    fclose(fpointer);
    return 0;
}
