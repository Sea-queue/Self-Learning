#include<stdio.h>
int main(){
    int age = 10;
    int *page = &age;
    double gpa = 4.0;
    double *pgpa = &gpa;
    char grade = 'A';
    char *pgrade = &grade;
    printf("%p\n", &age);
    printf("%p\n", &gpa);
    printf("%p\n", &grade);
    printf("%p\n%p\n%p\n", &age, &gpa, &grade);
    printf("%d\n%f\n%c\n%c\n", *page, *pgpa, *pgrade, *&grade);
}
