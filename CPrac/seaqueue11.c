#include<stdio.h>
/* switch function */
int main(){
    char grade;
    printf("Enter your grade: ");
    scanf(" %c", &grade);
    switch(grade){
    case 'A' | 'a' :
        printf("You did great\n");
        break;
    case 'B' | 'b':
        printf("You did poorly\n");
        break;
    case 'C' | 'c':
        printf("You did badly\n");
        break;
    case 'D' | 'd':
        printf("You did horrible\n");
        break;
    case 'F' | 'f':
        printf("You failed\n");
        break;
    default :
        printf("You should not be a studnet!\n");
    }
}
