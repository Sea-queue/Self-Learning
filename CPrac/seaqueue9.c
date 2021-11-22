#include<stdio.h>
#include<stdlib.h>
#include<math.h>
/* printf function */

int main(){
  char characterName[] = "Freddy";
  int characterAge = 21;
  printf("There is a man \"named\" %s\n", characterName);
  printf("He was %d years old\n", characterAge);
  characterAge = 75;
  printf("He really liked the name %s\n", characterName);
  printf("but did not like being %d\n", characterAge);

  int favnum = 7;
  printf("My favorite number is %d\n", favnum);
  printf("My favorite %s is %d\n","fruit", favnum);
  printf("%f\n", 3.14 + 5.4);
  printf("%f\n", pow(2, 3));
  printf("%f\n", floor(3.4));
  printf("%f\n", ceil(3.4));
  const int FAV_NUM = 5;
}
