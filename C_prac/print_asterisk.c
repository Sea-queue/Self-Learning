#include <stdio.h>

//Prints a triangle of asterisks with the base of a given interger from user
int main() {
   int i, space, rows, k;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = 1; i <= rows; ++i, k = 0) {
      for (space = 1; space <= rows - i; ++space) {
         printf("  ");
      }
      while (k != 2 * i - 1) {
         printf("* ");
         ++k;
      }
      printf("\n");
  }
}

/*
#include <stdio.h>

int main() {
    int rows, k;
    printf("Enter number of rows you want: ");
    scanf("%d", &rows);
    for (int i = 1; i <= rows; i++, k = 0) {
        for (int space = 1; space <= rows - i; space++){
            printf("  ");
        }
        while(k != 2 * i - 1){
            printf("* ");
            ++k;
        }
        printf("\n");
    }
    return 0;
}
*/
