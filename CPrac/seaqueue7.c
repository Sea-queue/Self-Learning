#include <stdio.h>
#include <string.h>
/* copy and paste */

int main () {
   char src[50], dest[50];

   strcpy(src,  "queue");
   strcpy(dest, "Sea");

   strcat(dest, src);

   printf("%s\n", dest);
}
