#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void q10(int** p_p_a){
    **p_p_a = 46; // dereference twice
}
void q11(int **p_p_a) {
    int *block = (int *)malloc(sizeof(int)); // this does not need to be two lines
    *p_p_a = block;
}
int main (){ 
    int a = 34;
    int *p_a = &a;
    q6(&p_a);
    printf("%d", a);
    return 0;
}