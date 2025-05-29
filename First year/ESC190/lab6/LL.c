#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next; // store location of the next node
} node;

typedef struct LL {
    int size; // size of linked linked list
    node *head; // store location of first node
} LL;

void create_node(node **p_n, int data) {
    *p_n = (node *)malloc(sizeof(node)); // make space for a node
    (*p_n)->data = data;
    (*p_n)->next = NULL; 
}

void create_LL_from_data(LL **p_LL, int *data_arr, int size) {
    // make space
    (*p_LL) = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0; // initialize size

    // keep track of last node in linked list
    node *tail = NULL; // set to NULL initially since there are no nodes in the list yet
    for (int i = 0; i < size; ++i) {
        node *n; // create a node so we can fill it up
        create_node(&n, data_arr[i]);
         
        // if last node is the first node
        if (tail == NULL) {
            (*p_LL)->head = n;
        }
        else { // last node is not the first node
            tail->next = n; // next node is n
        }
        // update the tail
        tail = n; // tail always is the last node
        // update size
        (*p_LL)->size += 1;
    }
}
void print_LL(LL *p_L) {
    node *current = p_L->head; // start at the first node
    while (current != NULL) {
        printf("%d", current->data);
        // update current
        current = current->next;
    }
    printf("\t end of list!");
}
int main () {
    int arr[] = {1,2,3,4,5,6,7,8,9}; // convert this to a linked list
    int size = sizeof(arr)/sizeof(arr[0]);

    LL *p_LL; // pointer to the linked list 
    create_LL_from_data(&p_LL, arr, 5);
    print_LL(p_LL);
    

    return 0;
}
