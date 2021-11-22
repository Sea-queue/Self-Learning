#include<stdio.h>
#include<string.h>
#define making_friends(a) printf(#a" Can we be friends? ")
/* making friends record */
int main(){
    char name1[50];
    char answer[20];
    int number[20];
    char Yes[] = "Yes";
    char yes[] = "yes";
    char Sure[] = "Sure";
    char sure[] = "sure";
    //printf("File :%s\n", __FILE__);
    printf("\nHey, what's your name?: ");
    scanf("%s", name1);
    printf("\nHey %s,", name1);
    making_friends( );
    scanf("%s", answer);
    if (strcmp(answer, Yes) == 0 || strcmp(answer, yes) == 0 || strcmp(answer, Sure) == 0 || strcmp(answer, sure) == 0){
        printf("\nGreat, let's hangout! Can I have your number? ");
        scanf("%d", number);
        printf("\nAwesome, I'll text you!");
    }
    printf("\n\nHere is our little record: ");
    printf("\nWe met on: %s", __DATE__);
    printf(" at %s!\n\n", __TIME__);

}
