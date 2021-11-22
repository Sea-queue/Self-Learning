#include<stdio.h>
#include<stdlib.h>
/* whiel function, do-while function, for-loop */

int main(){
    int index = 1;
    while(index <= 5){
        printf("%d\n", index);
        index++;
    }
    int in = 6;
    do {
        printf("%d\n", in);
        in++;
    }
    while(in <= 8);
    for(int i = 0; i <= 5; i++)
        printf("%d\n", i);
}
