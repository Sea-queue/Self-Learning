#include <stdio.h>
/* fahrenheit to celsius*/
int main(){
    printf("hello world\nSeaqueue's first C program\n");
    float fahr, celsius;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;
    fahr = lower;
    while (fahr <= upper){
        celsius = 5.0 * (fahr - 32) / 9.0;
        printf("%3.0f\t%6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
    printf("I LOVE YOU\n");
    for (fahr = 0; fahr <= upper; fahr = fahr + step)
        printf("%3.0f\t%6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
    printf("I HATE THAT I LOVE YOU\n");
    for (fahr = 300; fahr >= lower; fahr = fahr - step)
        printf("%3.0f\t%6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
}
