#include<stdio.h>

int main () {
    /* Playing with Pointers */
    int* pc, c;
    c = 5;
    pc = &c; // stores the address of c
    printf("%p \n", pc);
    printf("%d", *pc); // prints out 5, the value stored at the pointer. Here, the pointer is used as a "dereference operator", which means it outputs the value of an address




    return 0;
}