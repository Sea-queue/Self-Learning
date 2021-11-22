#include "stdio.h"
#include <string.h>

struct firstGen
{
    struct secondGen g2;
    struct thirdGen g3;
    struct fourthGen g4;
    char name[20];
    int age;
    char title[20];
    char livesIn[50];
};
struct sencondGen
{
    struct firstGen g1;
    struct thirdGen g3;
    struct fourthGen g4;
    char name[20];
    int age;
    char title[20];
    char livesIn[50];
};
struct thirdGen
{
    struct firstGen g1;
    struct secondGen g2;
    struct fourthGen g4;
    char name[20];
    int age;
    char title[20];
    char livesIn[50];
};
struct fourthGen
{
    struct firstGen g1;
    struct secondGen g2;
    struct thirdGen g3;
    char name[20];
    int age;
    char title[20];
    char livesIn[50];
};

int main() {
    struct firstGen fg = {"Cheng", 78, "Laoye", "Xilu"};
    struct secondGen sg[8];
    sg[1] = {"", , "", ""};
    sg[2] = {"", , "", ""};
    sg[3] = {"", , "", ""};
    sg[4] = {"", , "", ""};
    sg[5] = {"", , "", ""};
    sg[6] = {"", , "", ""};
    sg[7] = {"", , "", ""};
    sg[8] = {"", , "", ""};

    struct thirdGen tg[13];
    sg[1] = {"", , "", ""};
    sg[2] = {"", , "", ""};
    sg[3] = {"", , "", ""};
    sg[4] = {"", , "", ""};
    sg[5] = {"", , "", ""};
    sg[6] = {"", , "", ""};
    sg[7] = {"", , "", ""};
    sg[8] = {"", , "", ""};
    sg[9] = {"", , "", ""};
    sg[10] = {"", , "", ""};
    sg[11] = {"", , "", ""};
    sg[12] = {"", , "", ""};
    sg[13] = {"", , "", ""};

    struct fourthGen fg[4];
    sg[1] = {"ChengQian", 24, "Me", "USA"};
    sg[2] = {"", , "", ""};
    sg[3] = {"", , "", ""};
    sg[4] = {"", , "", ""};

    printf("em1: %s, %d, %s\n", em1.name, em1.age, em1.title);
    printf("em2: %s, %d, %s\n", em2.name, em2.age, em2.title);
    printf("em3: %s, %d, %s\n", em3.name, em3.age, em3.title);
}
