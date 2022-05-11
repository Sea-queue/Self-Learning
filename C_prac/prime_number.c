#include<stdio.h>
/* prime number */
int main(){
    int n, count, c;
    int i = 3;
    printf("How many prime number do you need?\n");
    scanf("%d\n", &n);
    if(n > 1){
        printf("2, ");
    }
    else{
        for(count = 2; count <= n; i++){
            for(c = 2; c < i; c++){
                if(i % c == 0){
                    break;
                }
                if (c == i){
                    printf("%d", i);
                    count++;
                }
            }
        }
    }
}
