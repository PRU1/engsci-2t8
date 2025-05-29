#include "linkedlist.h"
#include <stdio.h>
#include <stdlib.h>

void create_node(node **p_n, int data) { // use address of pointer to node
    // make space
    (*p_n) = (node *)malloc(sizeof(node));
    (*p_n)->data = data;
    (*p_n)->next = NULL;
}

int get_i(LL *p_LL, int i) { // for my ref, not lab

    // error handling
    if (p_LL->size <= i) {
        printf("element does not exist in linked list :(");
    }

    int j = 0; 
    node *cur = p_LL->head;
    while (j < i) {
        cur = cur->next;
        ++j;
    }
    return cur->data; // ran loop i times, so I'm at the ith node
    // O(n) time complexity
}

void LL_append(LL *my_list, int new_elem) {
    // case: you have an empty list
    node *new_node = (node *)malloc(sizeof(node)); // make space
    new_node->data = new_elem;
    new_node->next = NULL;

    if (my_list->size == 0) {
        my_list->head = new_node;
        my_list->size += 1;
        return;
    }
    // get to end of linked list
    node *cur = my_list->head;
    while (cur->next != NULL) { // traverse to the last valid node
        cur = cur->next;
    }

    // cur is now the tail node
    cur->next = new_node;
    my_list->size += 1;
}

int validate_list(LL *my_list) {
    int real_size = 0;
    node *cur = my_list->head;
    while (cur != NULL) {
        cur = cur->next;
        ++real_size;
    }
    if (real_size == my_list->size){
        return 1;
    }
    return 0;
}

void delete_node(LL *my_list, int index){
    // error handling
    if (index >= my_list->size) {
        printf("index out of bound");
        return;
    }
    node *cur = my_list->head;
    // delete head node
    if (index == 0) {
        my_list->head = cur->next;
        free(cur);
    }
    else {
        int j = 0; 
        while (j < index-1) {
            cur = cur->next;
            ++j;
        }
        // delete cur->next;
        node *temp = cur->next;
        cur->next = temp->next;
        free(temp);
    }
    my_list->size -= 1;
}

void print_linkedList(LL *my_list) {
    node *cur = my_list->head;
    while (cur != NULL) {
        printf("%d ", cur->data);
        cur = cur->next;
    }
}