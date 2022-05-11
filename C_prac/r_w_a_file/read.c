#include<stdio.h>
#include<stdlib.h>
int main(){
    char line[225];
    FILE * fpointer = fopen("cs240:\employees.txt", "r");
    fgets(line, 225, fpointer);
    //fgets(line, 225, fpointer);
    printf("%s", line);
    //fclose(fpointer);
    return 0;
}
