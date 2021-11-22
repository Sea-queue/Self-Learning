#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/* struct function */

struct Friend {
    char level[5];
    char place[50];
    char major[50];
};

struct Student{
    char  lover[50];
    char  major[50];
    int age;
    double leglength;
};

struct Books {
    char title[50];
    char author[50];
    char subject[50];
    int book_id;
};

void printBook(struct Friend friend){
    printf( "Friend level : %s\n", friend.level);
    printf( "Friend lives : %s\n", friend.place);
    printf( "Friend's major : %s\n", friend.major);
}

int main(){
    struct Student student1;
    student1.age = 22;
    student1.leglength = 1.2;
    strcpy(student1.lover, "Seaqueue");
    strcpy(student1.major, "CS");
    printf("student1's lover: %s\nMajor: %s\n", student1.lover, student1.major);

    struct Student student2;
    student2.age = 19;
    student2.leglength = 0.8;
    strcpy(student2.lover, "Po");
    strcpy(student2.major, "Chem");
    printf("student2's lover: %s\nMajor: %s\n", student2.lover, student2.major);

    struct Books book1;
    strcpy(book1.title, "Seaqueue' note");
    strcpy(book1.author, "Seaqueue");
    strcpy(book1.subject, "Life lessons");
    book1.book_id = 88888888;

    struct Books book2;
    strcpy(book2.title, "Learning A language");
    strcpy(book2.author, "Seaueue Cheng");
    strcpy(book2.subject, "Comunication");
    book2.book_id = 666666;

    printf("Book1 title: %s\n", book1.title);
    printf("Book2 subject: %s\n", book2.subject);
    printf("Book1 id: %d\n",book1.book_id);
    printf("Book2 author: %s\n",book2.author);


    return 0;
}
