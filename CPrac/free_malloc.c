#include <stdio.h>
#include <stdlib.h>

//example of malloc
int main(int argc, char **argv) {
    //this pointer will hold the base address of the block created
    int* ptr;
    int n, i;

    //get the number of elements for the array
    printf("Enter number of elements:");
    scanf("%d", &n);
    printf("Entered number of elements: %d\n", n);

    //Dynamically alloacted memory using malloc()
    ptr = (int*) malloc(n * sizeof(int));

    //Check if the memory has been successfully allocated by malloc
    if (ptr == NULL) {
        printf("Memory not allocated\n");
        exit(0);
    }

    else {
        //Memory has been successfully allocated
        printf("Memory successfully allocated using malloc.\n");

        //Get the elements of the array
        for (i = 0; i < n; i++) {
            ptr[i] = i + 1;
        }

        //print the elements of the array
        printf("The elements of the array are: ");
        for (i = 0; i < n; i++) {
            printf("%d, ", ptr[i]);
        }
    }

    free(ptr);
    printf("\nMalloc Memory successfully freed.\n");

    return 0;
}
