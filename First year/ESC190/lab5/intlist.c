#include "intlist.h"
#include <stdio.h>
#include <stdlib.h>

/*
typedef struct IntList {
    int *data;
    int size;
    int capacity;
} IntList;
*/

// Allocate memory for an object of type IntList, initialize
// its data to equal the data in data_arr, and set its size
// Store the address of the new object in *p_IntList
void create_list_from_data(IntList **p_IntList, int *data_arr, int size) {
    (*p_IntList) = (IntList *)malloc(sizeof(IntList)); // free up some space
    if (*p_IntList == NULL) {
        printf("Error : (");
        exit(1);
    }
    (*p_IntList)->size = 100;
    (*p_IntList)->capacity = 1000;
    (*p_IntList)->data = (int*)malloc(sizeof(int)*(*p_IntList)->capacity);
    if ((*p_IntList)->data == NULL){
        printf("ERROR : (");
        exit(1);
    }
    (*p_IntList)->data[size+1] = NULL;
}

// Append new_elem to the end of list
void list_append(IntList *list, int new_elem) {
    // check size of IntList
    if (list->size >= (list->capacity)) {
        // reallocate memory to create more space
        int new_capacity = list->capacity * 2;
        list->data = realloc(list->data,new_capacity);
        // define null character at end??
    }
    list->data[list->size+1] = new_elem;
    list->data[list->size+2] = NULL; // keep track of list end. Is this needed? try to optimize later. 
}


// Insert new_elem at index in list. new_elem should now be at
// location index.
// Use the function memmove to move elements of list->data as needed
// If the capacity needs to grow, use realloc to increase the capacity by
// a factor of 2
void list_insert(IntList *list, int new_elem, int index) {
    
}

// Delete the element at index index

void list_delete(IntList *list, int index);

// call free as appropriate to free the memory used by list
// Note: the order in which you free list->data and list
// itself is important (how?)
void list_destroy(IntList *list) {

}

// Return the element at index index in list
