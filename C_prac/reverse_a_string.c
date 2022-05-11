#include<stdio.h>
#include<string.h>
/* reverse a string */
int main(){
    int i, k;
    char string[50], temp;
    printf("What do you want to reverse on? ");
    scanf("%s", string);
    int l = strlen(string);
    for(i = 0; i < l / 2; i++){
        temp = string[i];
        string[i] = string[l - i];
        string[l - i] = temp;
    }
    for(k = 0; k <= l; k++)
        printf("%c", string[k]);
    printf("\n");
}
