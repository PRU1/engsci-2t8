#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.c"

int main () {
    LL hi; // initialization important or else your struct contains some random values
    hi.head = NULL;
    hi.size = 0;
    LL_append(&hi, 5);
    LL_append(&hi, 6);
    LL_append(&hi, 7);
    LL_append(&hi, 8);
    LL_append(&hi, 9);
    printf("%d \n", validate_list(&hi));
    delete_node(&hi, 2);
    print_linkedList(&hi);

    return 0;
}