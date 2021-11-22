#include <stdio.h>

/*
 C syntax for:
 array
 nested for loop on 2D array of numbers

*/
static void syntax() {

    //print out array of integers use a for loop
    int primenumber[] = {1, 3, 5, 7, 11, 13, 17,19};
    primenumber[0] = 23;
    for(int i = 0; i <= 8; i++){
      printf("%d ", primenumber[i]);
    }
    printf("%d\n", primenumber[0]);

    //print out 2D array of integers use nested for loop
    int num[3][2] = {{1, 2},{3, 4},{5, 6}};
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 3; j++){
            printf("%d, ", num[i][j]);
        }
        printf("\n");
    }
}
