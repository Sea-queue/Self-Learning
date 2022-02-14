#include <stdio.h>
#include <stdlib.h>

int main() {
    //This pointer will hold the base address of the block created
    int* ptr;
    int n, i;

    //get the number of elements for the array
    n = 5;
    printf("Enter number of elements: %d\n", n);

    //Dynamically allocated memory using calloc()
    ptr = (int*) calloc(n, sizeof(int));

    //Check if the memory has been successfully allocated by calloc
    if (ptr == NULL) {
        printf("Memory not allocated.\n");
        exit(0);
    }
    else {
        // Memory has been successfully allocated
        printf("Memory successfully allocated using calloc.\n");

        // Get the elements of the array
        for (i = 0; i < n; ++i) {
            ptr[i] = i + 1;
        }

        //Print the elements of the array
        printf("The elements of the array are: ");
        for (i = 0; i < n; ++i) {
            printf("%d, ", ptr[i]);
        }

        //get the new size for the array
        n = 10;
        ptr = realloc(ptr, n * sizeof(int));
        // Memory has been successfully allocated
        printf("\nMemory successfully re-allocated using realloc.\n");

        for (i = 5; i < n; i++) {
            ptr[i] = i + 1;
        }
        // Print the elements of the array
        printf("The elements of the array are: ");
        for (i = 0; i < n; ++i) {
            printf("%d, ", ptr[i]);
        }

        free(ptr);
    }

    return 0;
}
