#include <stdio.h>
#include <ctype.h>

//raise base to power n: power(2, 3) returns 8
static int power(int base, int n) {
    int p;
    // have to declare above for the return statment,
    // will be initialized to 1 even the n <= 0
    for(p = 1; n > 0; n -= 1)
        p = p * base;
    return p;
}

//check if the given variable is alphanumeric.
static void isAlphanumeric() {
    int var1 = '#';
    if (!isalnum(var1)) {
       printf("var1 = '%c' is not alphanumeric\n", var1 );
    } else {
       printf("var1 = '%c' is alphanumeric\n", var1 );
    }
}

//can calculate: double + - * / double.
static void calculator(){
    double num1;
    double num2;
    char op;
    printf("Enter a number: ");
    scanf("%lf", &num1);
    printf("Enter an operator: ");
    scanf(" %c", &op);
    printf("Enter a number: ");
    scanf("%lf", &num2);

    if(op == '+'){
        printf("%f\n", num1 + num2);
    }
    else if(op == '-'){
        printf("%f\n", num1 - num2);
    }
    else if(op == '*'){
        printf("%f\n", num1 * num2);
    }
    else if(op == '/'){
        printf("%f\n", num1 / num2);
    }
    else {
        printf("Your operator is out of my ability, my apology %c\n", op);
    }
}
