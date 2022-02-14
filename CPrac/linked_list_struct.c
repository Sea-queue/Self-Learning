
/*
 Lined list, each node points to another node and forming a chain, this is
 advantageous when compared to an array, because we can add or remove links as
 we need them -- thus we do not have to guess the size of data we need.

 Iterator pattern:
 we can traverse the linked list by using a 'iterator' pattern. That is we use
 a temporary node that points to each node. The 'iterator' then hops from the
 current node_t to node_t.next each iteration until next is NULL.
 */

#include <stdio.h>

 typedef struct node { // typede: so we do not have to type 'struct' everytime.
     int data;
     struct node* next;
 } node_t; // the 'typedef' name is specified as 'node_t' here.

//using the struct
int main(int argc, char **argv) {
    //Create a first node
    node_t node1;
    node1.data = 100;

    //Create a second node
    node_t node2;
    node2.data = 200;

    //Link the nodes together
    //node1 points to the address of node2
    node2.next = &node2;

    //node2 does not have a next node, so set it to NULL.
    node2.next = NULL;

    //iterating through the nodes
    node_t* iterator;

    //point to the first node(the head of the list)
    iterator = &node1;

    //While the iterator is not NULL, continue
    while(iterator != NULL) {
        //Print myData, which is the head in the first iteration.
        printf("%d\n", iterator->data);

        //Then move our iterator to whatever our 'next' node is in the linked list.
        iterator = iterator->next;
    }

    return 0;
}
