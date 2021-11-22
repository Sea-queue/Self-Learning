#include<stdio.h>
#include<stdlib.h>
int main(){
    FILE * fpointer = fopen("report5.txt", "w");
    fprintf(fpointer, "a): The optional command line arguments provide a sample of m and n");
    fprintf(fpointer, "\nfor the system to use both quick and counting sort methods to sort.");
    fprintf(fpointer, "\nb): {01220032320231013203213120213323123340022313122100211240123122}");
    fprintf(fpointer, "\nc): {987063541256}");
    fprintf(fpointer, "\nd): Quick sort compares elements from both ends and divides an array");
    fprintf(fpointer, "\ninto two smaller arrays, and then compares elements in both arrays and divides");
    fprintf(fpointer, "\ntwo smaller arrays into four even smaller arrays until the array is sorted.");
    fprintf(fpointer, "\nOn the other hand, counting sort goes through the array once, and counts how");
    fprintf(fpointer, "\nmany different elements are in the array, then prints the different elements in");
    fprintf(fpointer, "\norder accordingly with their amount. When the elements are vary, quick sort");
    fprintf(fpointer, "\nis faster because majority elements need to change their position to be in the");
    fprintf(fpointer, "\nright place, so the comparison in quick sort is meaningful. However, if");
    fprintf(fpointer, "\nin an array, most of the elements are repetitive, comparing the elements with the");
    fprintf(fpointer, "\nsame value is wasting time. In this case, quick sort performs many unnecessary");
    fprintf(fpointer, "\ncomparison. Therefore, counting sort makes more sense to count the");
    fprintf(fpointer, "\namount of the same type then simply use a for loop to print them out at once.");
    fclose(fpointer);
    return 0;
}
