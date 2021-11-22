#include<stdio.h>
/* days converting to years */
int main(){
    int numofdays, year, month, day;
    printf("\nHow many days do you want to convert? ");
    scanf("%d", &numofdays);
    year = (int)numofdays / 365;
    month = (int)(numofdays - year * 365) / 30;
    day = (numofdays - year * 365 - month * 30);
    printf("It is %dyears / %dmonths / %ddays\n", year, month, day);
}
