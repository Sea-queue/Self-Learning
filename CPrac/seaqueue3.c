#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* split the spending one paid for others */
int main() {
    printf("\n");
    printf("\n");
    printf("     *************\n");
    printf("   *    --------   *\n");
    printf(" *     @        @    *\n");
    printf("*           ^         *\n");
    printf(" *      - _ _ _ -    *\n");
    printf("   *               *\n");
    printf("     *************\n");
    printf("\n");
    printf("\n");
    printf("Don't be careless! Small accumalets to big!");
    char a;
    scanf("%c", &a);
    printf("\n");
    char A[20];
    char B[20];
    char C[20];
    char D[20];
    char E[20];
    char F[20];
    int Number_of_People;
    int Number_of_spents;
    double amount1;
    double amount2;
    double amount3;
    double amount4;
    double amount5;
    double amount6;
    double sum;
    double B_own_A = 0;
    double A_own_B = 0;
    double C_own_A = 0;
    double A_own_C = 0;
    double D_own_A = 0;
    double A_own_D = 0;
    double E_own_A = 0;
    double A_own_E = 0;
    double F_own_A = 0;
    double A_own_F = 0;
    printf("Who is this?\n");
    scanf("%s", A);
    printf("\nYo, thank you %s! How many spends are there?\n", A);
    scanf("%d", &Number_of_spents);
    if (Number_of_spents == 1){
        printf("Enter the amounts and press return after each one.\n");
        scanf("%lf", &amount1);
        sum = amount1;
    }
    if (Number_of_spents == 2){
        printf("Enter the amounts and press return after each one.\n");
        scanf("%lf", &amount1);
        scanf("%lf", &amount2);
        sum = amount1 + amount2;
    }
    if (Number_of_spents == 3){
        printf("Enter the amounts and press return after each one.\n");
        scanf("%lf", &amount1);
        scanf("%lf", &amount2);
        scanf("%lf", &amount3);
        sum = amount1 + amount2 + amount3;
    }
    if (Number_of_spents == 4){
        printf("Enter the amounts and press return after each one.\n");
        scanf("%lf", &amount1);
        scanf("%lf", &amount2);
        scanf("%lf", &amount3);
        scanf("%lf", &amount4);
        sum = amount1 + amount2 + amount3 + amount4;
    }
    if (Number_of_spents == 5){
        printf("Enter the amounts and press return after each one.\n");
        scanf("%lf", &amount1);
        scanf("%lf", &amount2);
        scanf("%lf", &amount3);
        scanf("%lf", &amount4);
        scanf("%lf", &amount5);
        sum = amount1 + amount2 + amount3 + amount4 + amount5;
    }

    printf("How many people own you?\n");
    scanf("%d", &Number_of_People);
    if (Number_of_People == 1){
        printf("Who is this lucky girl or boy?\n");
        scanf("%s", B);
        B_own_A = sum / 2;
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", B, A, B_own_A);
    }
    if (Number_of_People == 2){
        printf("Who are they?\n");
        scanf("%s", B);
        scanf("%s", C);
        B_own_A = sum / 3;
        C_own_A = sum / 3;
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", B, A, B_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n\n", B, A, C_own_A);
    }
    if (Number_of_People == 3){
        printf("Who are they?\n");
        scanf("%s", B);
        scanf("%s", C);
        scanf("%s", D);
        B_own_A = sum / 4;
        C_own_A = sum / 4;
        D_own_A = sum / 4;
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", B, A, B_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", C, A, C_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n\n", D, A, D_own_A);
    }
    if (Number_of_People == 4){
        printf("Who are they?\n");
        scanf("%s", B);
        scanf("%s", C);
        scanf("%s", D);
        scanf("%s", E);
        B_own_A = sum / 5;
        C_own_A = sum / 5;
        D_own_A = sum / 5;
        E_own_A = sum / 5;
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", B, A, B_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", C, A, C_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", D, A, D_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n\n", D, A, E_own_A);
    }
    if (Number_of_People == 5){
        printf("Who are they?\n");
        scanf("%s", B);
        scanf("%s", C);
        scanf("%s", D);
        scanf("%s", E);
        scanf("%s", F);
        B_own_A = sum / 6;
        C_own_A = sum / 6;
        D_own_A = sum / 6;
        E_own_A = sum / 6;
        F_own_A = sum / 6;
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", B, A, B_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", C, A, C_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", D, A, D_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n", D, A, E_own_A);
        printf("\nUpdate: { %s owns %s $%f ^_^}\n\n", D, A, F_own_A);
    }

    return 0;
}
