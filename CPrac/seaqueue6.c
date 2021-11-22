#include<stdio.h>
/*
Math:
multiplication table;
power calculation;
sum;
factors of a number;
max;
*/
int main(){
    int k, m;
    double input;
    double fact = 1;
    double sum = 0;
    double l;
    printf("Which number of table do you want to find? Enter: ");
    scanf("%lf", &input);
    printf("\nTable of %f:\n", input);
    for(int i = 1; i < 10; i++)
        printf("%f\n", input * i);

    int p;
    double result = 1;
    printf("Enter the base number:");
    scanf("%lf", &input);
    printf("Enter a power number:");
    scanf("%d", &p);
    for (int i = 1; i <= p; i++)
        result = result * input;
    printf("%f to the power of %d is: %f\n", input, p, result);

    printf("\nSum of 1 through %f is:\n", input);
    for (int i = 1; i <= input; i++)
        sum +=i;
    printf("%f\n", sum);

    printf("\nFind the factors of the number: ");
    scanf("%d", &m);
    printf("Factors of %d are: ", m);
    for (int i = 1; i < m; i++)
        if(m % i == 0)
            printf("%d ", i);
    printf("\n");
    int main(){
        int i = 1;
        int j = 2;
        int k = 3;
        printf("%d\n", max3(i, j, k));
    }
}
int Factorial(double input){
    if (input == 0)
        return 1;
    else
        return input * Factorial(input - 1);
}
/*
Max bumber: 
#include<stdio.h>
#define max(A, B) ((A) > (B) ? (A) : (B))
#define max3(A, B, C) (max(A, B) > (C) ? max(A, B) : (C))
int main(){
    int i = 1;
    int j = 2;
    int k = 3;
    printf("%d\n", max3(i, j, k));
}
*/
