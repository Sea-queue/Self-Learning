/*
$: The way it stores data
$: The way it operates on this data
$: The way it accomplishes input and output
$: The way to let me control the sequence of execution of instructions
*/

/*
sending and receiving values between functions
*/

int i;
int x = 21;

#include <stdio.h>
#include <math.h>
#include <string.h>

#define AND &&
#define OR ||
#define ARANGE (a > 25 AND a < 50)
#define FOUND printf("The yankee Doodle Virus\n");
#define SQUARE(n) (n * n);

struct book {
    char name[25];
    char author[25];
    int callno;
};

int main() {
    //reserve space in memory to hold the integer value;
    //Associate the name i with this memory location;
    //Store the value 3 at this location
    //int i = 3;
    //pointer variables: variable capable of holding addresses

    //pointer varable
    /*
    int *j, **k;
    j = &i;
    k = &j;
    */

    //function declaration, notice how to declare the pointer in a fucntion
    /*
    void areaperi(int, float *, float *);

    int radius;
    float area, perimeter;

    printf("Enter radius of a circle\n");
    scanf("%d", &radius);
    areaperi(radius, &area, &perimeter);

    printf("Area = %f\n", area);
    printf("Perimeter = %f\n", perimeter);
    */

    //extern int y;
    //printf("%d\n%d\n", x, y);

    struct book {
        char name[25];
        char author[25];
        int callno;
    };

    struct book b1 = {"Let us C", "YPK", 101};
    struct book *ptr;

    ptr = &b1;

    printf("%s %s %d\n", b1.name, b1.author, b1.callno);
    printf("%s %s %d\n", ptr->name, ptr->author, ptr->callno);

    char *check = "good";
    printf("check = %s\n", check); 
    
   
}

void linkfloat() {
    float a = 0, *b;
    b = &a;
    a = *b;
}

int y = 31;

/*
We have been able to indirectly return two values from a called function,
and hence, have overcome the limitation of the return statement, which can
return only one value from a function at a time.
*/
void areaperi (int r, float *a, float *p) {
    *a = 3.14 * r * r;
    *p = 2 * 3.14 * r;
}


//return the factorial of the given number with for loop
int factorial(int x) {
    int f = 1;
    for (int i = x; i >= 1; i -= 1) {
        f = f * i;
    }
    return f;
}

//return the factorial of the given number with recursive call
int recFactorial(int x) {
    int f;
    if (x == 1) {
        return 1;
    }
    else {
        f = x * recFactorial(x - 1);
    }
    return f;
}

//add the given two numbers
int add(int i, int j) {
    int sum;
    sum = i + j;
    return sum;
}

//prints out the increments with auto storage
void autoIncrement() {
    auto int i = 1;
    printf("%d\n", i);
    i = i + 1;
}

//prints out the increments with static storage
void staticIncrement() {
    static int i = 1;
    printf("%d\n", i);
    i = i + 1;
}


void increment() {
    i = i + 1;
    printf("on incrementing i = %d\n", i);
}

void decrement() {
    i = i - 1;
    printf("on decrementing i = %d\n", i);
}


//display the given info
void display(struct book b) {
    printf("%s, %s, %d\n", b.name, b.author, b.callno);
}
