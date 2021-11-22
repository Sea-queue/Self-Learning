#include<stdio.h>
#include<string.h>
/* little fun game */
int main(){
    int k, m;
    char p[] = "yes";
    char l[3];
    int comp;
    printf("\nHey, welcome to the show!");
    //Wait for user to hit enter before quitting
    getchar();
    /*char a;
    scanf("%c", &a);*/
    printf("\n");
    printf("Enter a number: k =  ");
    scanf("%d", &k);
    printf("\nEnter another number: m = ");
    scanf("%d", &m);
    printf("\nAre you ready for the mageic?: ");
    scanf("%s", l);
    comp = strcmp(l, p);
    if (comp > 0){
        k = k + m;
        m = k - m;
        k = k - m;
        printf("\nk = %d, m = %d\n", k, m);
        getchar();
        printf("\nBang! Swapped!\n");
    }
    else
        printf("\nWhenever you ready!\n");

    char yes[] = "yes";
    char sure[] = "sure";
    char okay[] = "okay";
    char kiss[] = "kiss";
    char blank[] = "no";
    char play[9];
    char kos[9];
    char j[9];
    char fol[9];
    char fine[9];
    printf("\nDo you want play a game?: ");
    scanf("%s", play);
    if (strcmp(play, yes) == 0 || strcmp(play, sure) == 0 || strcmp(play, okay) == 0){
        printf("\nOkay, here is one, kiss or slap? ");
        scanf("%s", kos);
        if (strcmp(kos, kiss) == 0){
            printf("\nFrench or lay down? ");
            scanf("%s", fol);
            if (strcmp(fol, blank) == 0){
                printf("\n(o * o)\n\nthink again? ");
                scanf("%s", fine);
                if (strcmp(fine, blank) == 0)
                    printf("\nJust kidding. Here, on my cheek.\n");
            }
        }
        else
            printf("\nNo ): ): ): Okay fine, go head!\n\n");
    }
    else {
        printf("\nYou asshole! What do you want? ");
        scanf("%s", j);
        printf("\nOkay! Fine.\n");
    }
}
